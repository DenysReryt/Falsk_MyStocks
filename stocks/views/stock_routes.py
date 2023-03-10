from flask import render_template, Blueprint, redirect, request, url_for, flash
import requests
from requests.exceptions import JSONDecodeError

stock_bp = Blueprint('stocks', __name__, url_prefix='/stocks')
base_url = 'http://localhost:5000/api/stocks'
headers = {'Content-Type': 'application/json'}


# Get a list of all stocks
@stock_bp.route('', methods=['GET'])
def list_stocks():
    try:
        response = requests.get(base_url).json()
        return render_template('stocks.html', stocks=response)
    except JSONDecodeError:
        return render_template('stocks.html')


# Get one stock by id
@stock_bp.route('/<int:stock_id>', methods=['GET'])
def get_stock(stock_id: int):
    response = requests.get(base_url + f'/{stock_id}').json()
    return response


# Create new stock
@stock_bp.route('', methods=['POST'])
def create_stock():
    company = request.form.get('company')
    sector = request.form.get('sector')
    amount = request.form.get('amount')
    price = request.form.get('price')
    data = {'company': company, 'sector': sector, 'amount': amount, 'price': price}
    response = requests.post(base_url, headers=headers, json=data).json()
    if response is False:
        flash('This company is already selling stocks.')
    else:
        flash(f'Company {company} added successfully.', 'success')
    return redirect(url_for('stocks.list_stocks'))


# Update stock
@stock_bp.route('/<int:stock_id>', methods=['GET', 'POST'])
def update_stock(stock_id: int):
    if request.method == 'POST':
        amount = request.form.get('amount')
        price = request.form.get('price')
        data = {'amount': int(amount), 'price': float(price)}
        response = requests.put(base_url + f'/{stock_id}', headers=headers, json=data).json()
        flash(f'Stock {stock_id} updated successfully.', 'success')
        return redirect(url_for('stocks.list_stocks'))


# Delete Stock
@stock_bp.route('/<int:stock_id>', methods=['DELETE'])
def delete_stock(stock_id: int):
    response = requests.delete(base_url + f'/{stock_id}')
    flash('Stock deleted successfully.', 'success')
    return redirect(url_for('stocks.list_stocks'))
