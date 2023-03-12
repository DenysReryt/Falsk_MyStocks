"""Module with RESTful for stocks CRUD"""
from typing import Tuple, Any, Union, Dict
import json

from flask_restful import Resource
from flask import request
from sqlalchemy.exc import IntegrityError

from stocks.service import stock_crud


class StockListRes(Resource):
    """
        Resource class for listing stocks and creating new stocks.
    """

    def get(self) -> Tuple[Any, int]:
        """Get a list of all stocks"""
        stocks = stock_crud.get_all_stocks()
        stocks_list = [stock.to_dict() for stock in stocks]
        json_str = json.dumps(stocks_list)
        return json.loads(json_str), 200

    def post(self) -> Union[Tuple[Any, int], bool]:
        """Create a new stock"""
        try:
            data = request.get_json()
            company = data.get('company')
            sector = data.get('sector')
            amount = data.get('amount')
            price = data.get('price')
            stock = stock_crud.create_stock(company=company, sector=sector, amount=amount, price=price)
            json_str = json.dumps(stock.to_dict())
            return json.loads(json_str), 201
        except IntegrityError:
            return False


class StockRes(Resource):
    """
        Resource class for update get delete specific stocks.
    """

    def get(self, stock_id: int) -> Union[Tuple[Dict[str, str], int], Tuple[Any, int]]:
        """Get a stock by ID"""
        stock = stock_crud.get_stock(stock_id=stock_id)
        if not stock:
            return {'message': 'Stock not found'}, 404
        json_str = json.dumps(stock.to_dict())
        return json.loads(json_str), 200

    def put(self, stock_id: int) -> Union[Dict[str, str], Tuple[Any, int]]:
        """Update a stock by ID"""
        data = request.get_json()
        amount = data.get('amount')
        price = data.get('price')
        current_amount = stock_crud.get_stock(stock_id=stock_id)
        if current_amount is None:
            return {'message': 'Stock not found'}
        json_str_amount = current_amount.to_dict()
        total = json_str_amount['amount'] + int(amount)
        stock = stock_crud.update_stock(stock_id=stock_id, amount=total, price=price)
        json_str = json.dumps(stock.to_dict())
        return json.loads(json_str), 200

    def delete(self, stock_id: int) -> Tuple[Dict[str, str], int]:
        """Delete a stock by ID"""
        deleted = stock_crud.delete_stock(stock_id=stock_id)
        if deleted is False:
            return {'message': 'Stock not found'}, 404
        return {'message': 'Successfully deleted'}, 201
