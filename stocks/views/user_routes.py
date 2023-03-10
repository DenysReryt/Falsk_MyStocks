from flask import render_template, Blueprint, redirect, request, url_for, flash
import requests
from requests.exceptions import JSONDecodeError

user_bp = Blueprint('users', __name__, url_prefix='/users')
base_url = 'http://localhost:5000/api/users'
headers = {'Content-Type': 'application/json'}


# Get a list of all users
@user_bp.route('', methods=['GET'])
def list_users():
    try:
        response = requests.get(base_url).json()
        return render_template('users.html', users=response)
    except JSONDecodeError:
        return render_template('users.html')


# Get one user by id
@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    response = requests.get(base_url + f'/{user_id}').json()
    return render_template('user.html', users=response)


# Create new user
@user_bp.route('', methods=['POST'])
def create_user():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    phone = request.form.get('phone')
    data = {'first_name': first_name, 'last_name': last_name, 'phone': phone}
    response = requests.post(base_url, headers=headers, json=data).json()
    if response is False:
        flash('This phone number is already in use.')
    else:
        flash(f'User {first_name} {last_name} added successfully.', 'success')
    return redirect(url_for('users.list_users'))


# Update user
@user_bp.route('/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id: int):
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        phone = request.form.get('phone')
        data = {'first_name': first_name, 'last_name': last_name, 'phone': phone}
        response = requests.put(base_url + f'/{user_id}', headers=headers, json=data).json()
        if response is False:
            flash('This phone number is already in use.')
        else:
            flash(f'User {first_name} {last_name} updated successfully.', 'success')
        return redirect(url_for('users.list_users'))


# Delete User
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    response = requests.delete(base_url + f'/{user_id}')
    flash('User deleted successfully.', 'success')
    return redirect(url_for('users.list_users'))
