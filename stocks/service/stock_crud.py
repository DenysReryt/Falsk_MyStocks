"""Module for CRUD operations to work with stocks table"""
from typing import List, Optional
from stocks.models.models import db, Stock, UserStock


def get_all_stocks() -> List[Stock]:
    """
        Retrieve all stocks from the database
    """
    query = Stock.query
    return query.all()


def get_stock(stock_id: int) -> Optional[Stock]:
    """
        Retrieve a stock from the database by its ID.
    """
    return Stock.query.filter_by(id=stock_id).first()


def get_stock_by_company(company: str) -> Optional[Stock]:
    """
        Retrieve a stock from the database by its company name.
    """
    return Stock.query.filter_by(company=company).first()


def create_stock(company: str, sector: str, amount: int, price: float) -> Optional[Stock]:
    """
        Create a new stock and add it to the database.
    """
    stock = Stock(company=company, sector=sector, amount=amount, price=price)
    db.session.add(stock)
    db.session.commit()
    return stock


def update_stock(stock_id: int, amount: Optional[int] = None, price: Optional[float] = None) -> Optional[Stock]:
    """
        Update a stock in the database by its ID.
    """
    stock = Stock.query.filter_by(id=stock_id).first()
    if amount:
        stock.amount = amount
    if price:
        stock.price = price
    user_stock = UserStock.query.filter_by(stock_id=stock_id).all()
    for i in user_stock:
        k = int(i.stocks_amount) * price
        i.suma = round(k, 2)
        db.session.commit()
    return stock


def delete_stock(stock_id: int) -> int:
    """
        Delete a stock from the database by its ID.
    """
    stock = Stock.query.filter_by(id=stock_id).first()
    if not stock:
        return False
    db.session.delete(stock)
    db.session.commit()
