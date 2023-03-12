"""Module for CRUD operations to work with users_stocks"""
from typing import Optional
from stocks.models.models import db, UserStock, User, Stock


def get_all_user_stocks(user_id: int):
    """Get all user stocks for a given user ID."""
    return UserStock.query.filter_by(user_id=user_id).all()


def create_user_stock(stock_id: int, suma: float, user_id: int, company: str, stocks_amount: int) -> \
        Optional[UserStock]:
    """Create a new user stock."""
    user_stock = UserStock(stock_id=stock_id, suma=suma, user_id=user_id, company=company,
                           stocks_amount=stocks_amount)
    db.session.add(user_stock)
    users = UserStock.query.filter_by(user_id=user_id).all()
    k = 0
    for i in users:
        k += int(i.stocks_amount)
    user = User.query.filter_by(id=user_id).first()
    user.stocks_amount = k
    db.session.commit()
    return user_stock


def get_user_stock(user_id: int, stock_id: int) -> Optional[UserStock]:
    """Get a user stock for a given user ID and stock ID."""
    return UserStock.query.filter_by(user_id=user_id, stock_id=stock_id).all()


def delete_stock(user_stock_id: int, stock_id: int, user_id: int) -> int:
    """Delete a user stock."""
    query = UserStock.query.filter_by(user_id=user_id, stock_id=stock_id, id=user_stock_id).first()
    if not query:
        return False
    stock = Stock.query.filter_by(id=stock_id).first()
    stock.amount += query.stocks_amount
    user = User.query.filter_by(id=user_id).first()
    user.stocks_amount -= query.stocks_amount

    db.session.delete(query)
    db.session.commit()
