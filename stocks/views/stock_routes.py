"""This module contains routes related to stocks in a Flask application."""
from flask import render_template, Blueprint, redirect, request, url_for, flash
import requests
from requests.exceptions import JSONDecodeError

stock_bp = Blueprint('stocks', __name__, url_prefix='/stocks')
BASE_URL = 'http://localhost:5000/api/stocks'
headers = {'Content-Type': 'application/json'}


@stock_bp.route('', methods=['GET'])
def list_stocks():
    """
        Route to get a list of all stocks.
    """
    try:
        response = requests.get(BASE_URL, timeout=5).json()
        return render_template('stocks.html', stocks=response)
    except JSONDecodeError:
        return render_template('stocks.html')


@stock_bp.route('/<int:stock_id>', methods=['GET'])
def get_stock(stock_id: int):
    """
        Route to get a single stock by its ID.
    """
    response = requests.get(BASE_URL + f'/{stock_id}', timeout=5).json()
    return response


@stock_bp.route('', methods=['POST'])
def create_stock():
    """
        Route to create a new stock.
    """
    company = request.form.get('company')
    sector = request.form.get('sector')
    amount = request.form.get('amount')
    price = request.form.get('price')
    data = {'company': company, 'sector': sector, 'amount': amount, 'price': price}
    response = requests.post(BASE_URL, headers=headers, json=data, timeout=5).json()
    if response is False:
        flash('This company is already selling stocks.')
    else:
        flash(f'Company {company} added successfully.', 'success')
    return redirect(url_for('stocks.list_stocks'))


@stock_bp.route('/<int:stock_id>', methods=['GET', 'POST'])
def update_stock(stock_id: int):
    """
        Route to update an existing stock.
    """
    if request.method == 'POST':
        amount = request.form.get('amount')
        price = request.form.get('price')
        data = {'amount': int(amount), 'price': float(price)}
        requests.put(BASE_URL + f'/{stock_id}', headers=headers, json=data, timeout=5).json()
        flash(f'Stock {stock_id} updated successfully.', 'success')
        return redirect(url_for('stocks.list_stocks'))


@stock_bp.route('/<int:stock_id>', methods=['DELETE'])
def delete_stock(stock_id: int):
    """
        Route to delete an existing stock.
    """
    requests.delete(BASE_URL + f'/{stock_id}', timeout=5)
    flash('Stock deleted successfully.', 'success')
    return redirect(url_for('stocks.list_stocks'))
