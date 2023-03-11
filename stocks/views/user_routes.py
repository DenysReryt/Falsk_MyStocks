"""This module contains routes related to users in a Flask application."""
from flask import render_template, Blueprint, redirect, request, url_for, flash
import requests
from requests.exceptions import JSONDecodeError

user_bp = Blueprint('users', __name__, url_prefix='/users')
BASE_URL = 'http://localhost:5000/api/users'
headers = {'Content-Type': 'application/json'}



@user_bp.route('', methods=['GET'])
def list_users():
    """
    Retrieves a list of all users from the API and renders them in a template.
    """
    try:
        response = requests.get(BASE_URL, timeout=5).json()
        return render_template('users.html', users=response)
    except JSONDecodeError:
        return render_template('users.html')


@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    """
    Retrieves a user by ID from the API.
    """
    response = requests.get(BASE_URL + f'/{user_id}', timeout=5).json()
    return response



@user_bp.route('', methods=['POST'])
def create_user():
    """
    Creates a new user with the provided data and redirects to the user list.
    """
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    phone = request.form.get('phone')
    data = {'first_name': first_name, 'last_name': last_name, 'phone': phone}
    response = requests.post(BASE_URL, headers=headers, json=data, timeout=5).json()
    if response is False:
        flash('This phone number is already in use.')
    else:
        flash(f'User {first_name} {last_name} added successfully.', 'success')
    return redirect(url_for('users.list_users'))



@user_bp.route('/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id: int):
    """
    Updates a user with the provided data and redirects to the user list.
    """
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        phone = request.form.get('phone')
        data = {'first_name': first_name, 'last_name': last_name, 'phone': phone}
        response = requests.put(BASE_URL + f'/{user_id}', headers=headers, json=data, timeout=5).json()
        if response is False:
            flash('This phone number is already in use.')
        else:
            flash(f'User {first_name} {last_name} updated successfully.', 'success')
        return redirect(url_for('users.list_users'))



@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    """
    Deletes a user by ID and redirects to the user list.
    """
    requests.delete(BASE_URL + f'/{user_id}', timeout=5)
    flash('User deleted successfully.', 'success')
    return redirect(url_for('users.list_users'))
