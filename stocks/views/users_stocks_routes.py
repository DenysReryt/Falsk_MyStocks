"""This module contains routes related to users_stocks in a Flask application."""
from flask import render_template, Blueprint, redirect, request, url_for, flash
import requests

user_stock_bp = Blueprint('users_stocks', __name__, url_prefix='/users/stocks')
BASE_URL = 'http://localhost:5000/api/users/stocks'                                     #users_stocks
headers = {'Content-Type': 'application/json'}


@user_stock_bp.route('/<int:user_id>', methods=['GET'])
def list_user_stocks(user_id: int):
    """
    Retrieve a list of user's stocks.
    """
    try:
        response = requests.get(BASE_URL + f'/{user_id}', timeout=5).json()
        stocks = requests.get('http://localhost:5000/api/stocks', timeout=5).json()
        return render_template('user.html', user_stocks=response, user_id=user_id, stocks=stocks)
    except TypeError:
        return render_template('user.html', response=[], user_id=user_id, stocks=stocks)


@user_stock_bp.route('/<int:user_id>', methods=['POST'])
def buy_stock(user_id: int):
    """
    Buy stocks for a user.
    """
    company = request.form.get('company')
    stocks_amount = request.form.get('stocks_amount')
    data = {'company': company, 'stocks_amount': int(stocks_amount)}
    response = requests.post(BASE_URL + f'/{user_id}', headers=headers, json=data, timeout=5).json()
    if response == {'message': 'Too many stocks to buy.'}:
        flash('Too many stocks to buy.')
    elif response is None:
        flash("There are no company with this name.")
    elif response is False:
        flash("There are no company with this name.")
    else:
        flash('Successfully bought')
    return redirect(url_for('users_stocks.list_user_stocks', user_id=user_id))


@user_stock_bp.route('/<int:user_id>/<int:stock_id>', methods=['GET'])
def get_stock(user_id: int, stock_id: int):
    """
    Retrieve details of a user's specific stock.
    """
    response = requests.get(BASE_URL + f'/{user_id}/{stock_id}', timeout=5).json()
    return response


@user_stock_bp.route('/<int:user_id>/<int:stock_id>/<int:user_stock_id>', methods=['DELETE'])
def delete_stock(user_id: int, stock_id: int, user_stock_id: int):
    """
    Delete a user's specific stock.
    """
    requests.delete(BASE_URL + f'/{user_id}/{stock_id}/{user_stock_id}', timeout=5)
    flash('Stock deleted successfully.', 'success')
    return redirect(url_for('users_stocks.list_user_stocks'))
