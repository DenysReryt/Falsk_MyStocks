"""
Module containing SQLAlchemy models.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class User(db.Model):
    """Model for the 'users' table."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    stocks_amount = db.Column(db.Integer, default=0)
    registration_date = db.Column(db.DateTime, server_default=func.now())
    phone = db.Column(db.String(15), nullable=False, unique=True)

    def to_dict(self):
        """Return the model properties as a dictionary."""
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'stocks_amount': self.stocks_amount,
            'registration_date': self.registration_date,
            'phone': self.phone
        }


class Stock(db.Model):
    """Model for the 'stocks' table."""

    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(50), nullable=False, unique=True)
    sector = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)

    def to_dict(self):
        """Return the model properties as a dictionary."""
        return {
            'id': self.id,
            'company': self.company,
            'sector': self.sector,
            'amount': self.amount,
            'price': self.price
        }


class UserStock(db.Model):
    """Model for the 'users_stocks' table."""

    __tablename__ = 'users_stocks'

    id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.Integer, db.ForeignKey('stocks.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    company = db.Column(db.String(50), db.ForeignKey('stocks.company'))
    stocks_amount = db.Column(db.Integer, nullable=False)
    suma = db.Column(db.Float(precision=2), nullable=False)

    def to_dict(self):
        """Return the model properties as a dictionary."""
        return {
            'id': self.id,
            'stock_id': self.stock_id,
            'user_id': self.user_id,
            'company': self.company,
            'stocks_amount': self.stocks_amount,
            'suma': self.suma,
        }
