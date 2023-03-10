from typing import Tuple, Any, Optional, Union, Dict

from flask_restful import Resource
from flask import request
from stocks.service.users_stocks_crud import user_stock_crud
from stocks.service.stock_crud import stock_crud
import json
from sqlalchemy.exc import IntegrityError


class UserStockListRes(Resource):
    def get(self, user_id: int) -> Optional[Tuple[Any, int]]:
        """Get all the stocks of a user."""
        user_stocks = user_stock_crud.get_all_user_stocks(user_id=user_id)
        if user_stocks:
            user_stocks_list = [user_stock.to_dict() for user_stock in user_stocks]
            json_str = json.dumps(user_stocks_list)
            return json.loads(json_str), 200
        return None

    def post(self, user_id: int) -> Union[bool, Tuple[Dict[str, str], int], Tuple[Any, int], Dict[str, str]]:
        """Buy stocks for a user."""
        try:
            data = request.get_json()
            company = data.get('company')
            stocks_amount = data.get('stocks_amount')
            stock = stock_crud.get_stock_by_company(company=company)
            if stock is None:
                return False
            else:
                if stock.amount < stocks_amount:
                    return {'message': 'Too many stocks to buy.'}, 403
                else:
                    total_suma = round(int(stocks_amount) * float(stock.price), 2)
                    user_stocks = user_stock_crud.create_user_stock(stock_id=stock.id, suma=total_suma,
                                                                    user_id=user_id,
                                                                    company=company, stocks_amount=stocks_amount)
                    sub = int(stock.amount) - int(stocks_amount)
                    stock_crud.update_stock(stock_id=stock.id, amount=sub,
                                            price=stock.price)
                    json_str = json.dumps(user_stocks.to_dict())
                    return json.loads(json_str), 201
        except IntegrityError as e:
            return {'error': str(e)}

class UserStockRes(Resource):
    """Class to work with information about every user's bought"""
    def get(self, user_id: int, stock_id: int) -> Tuple[Any, int]:
        """Get the details of a user's stock."""
        stocks = user_stock_crud.get_user_stock(user_id=user_id, stock_id=stock_id)
        stocks_list = [stock.to_dict() for stock in stocks]
        json_str = json.dumps(stocks_list)
        return json.loads(json_str), 200

class UserStockDel(Resource):
    """Class to delete user's stock by them id"""
    def delete(self, user_id: int, stock_id: int, user_stock_id: int) -> Tuple[Dict[str, str], int]:
        """Delete user's stock by id, user_id and stock_id."""
        payload = user_stock_crud.delete_stock(id=user_stock_id, stock_id=stock_id, user_id=user_id)
        if payload == 0:
            return {'message': 'Stock not found'}, 404
        return {'message': 'Successfully deleted'}, 201
