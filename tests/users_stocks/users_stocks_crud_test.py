import unittest
from unittest.mock import patch, MagicMock

from stocks.main import app
from stocks.config import settings
from stocks.models.models import UserStock, User, Stock
from stocks.service.users_stocks_crud import create_user_stock, delete_stock, get_user_stock, get_all_user_stocks


class TestUsersStocksCrud(unittest.TestCase):
    def setUp(self):
        self.user1 = User(id=1, first_name="User 1")
        self.stock1 = Stock(id=1, company="Stock 1", amount=100)
        self.user_stock1 = UserStock(id=1, stock_id=1, suma=100.00, user_id=1, company="Stock 1", stocks_amount=10)
        self.user_stock2 = UserStock(id=2, stock_id=1, suma=200.00, user_id=1, company="Stock 1", stocks_amount=20)

        app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
        app.config['TESTING'] = True
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        # Remove the Flask application context
        self.app_context.pop()

    @patch('stocks.service.users_stocks_crud.UserStock.query')
    def test_get_all_user_stocks(self, mock_query):
        mock_query.filter_by.return_value.all.return_value = [self.user_stock1, self.user_stock2]
        user_stocks = get_all_user_stocks(user_id=1)
        self.assertEqual(user_stocks, [self.user_stock1, self.user_stock2])

    @patch('stocks.service.users_stocks_crud.UserStock.query')
    def test_get_user_stock(self, mock_query):
        mock_query.filter_by.return_value.all.return_value = [self.user_stock1]
        user_stock = get_user_stock(user_id=1, stock_id=1)
        mock_query.filter_by.assert_called_once_with(user_id=1, stock_id=1)
        self.assertEqual(user_stock[0].id, 1)
        self.assertEqual(user_stock[0].stock_id, 1)
        self.assertEqual(user_stock[0].suma, 100.00)
        self.assertEqual(user_stock[0].user_id, 1)
        self.assertEqual(user_stock[0].company, "Stock 1")
        self.assertEqual(user_stock[0].stocks_amount, 10)

    @patch('stocks.service.users_stocks_crud.UserStock.query')
    @patch('stocks.service.users_stocks_crud.db.session')
    def test_create_user_stock(self, mock_session, mock_query):
        mock_query.filter_by.return_value.all.return_value = [self.user_stock1]
        user_stock = create_user_stock(stock_id=1, suma=300.00, user_id=1, company="Test Company 3", stocks_amount=30)
        mock_query.filter_by.assert_called_once_with(user_id=1)
        mock_session.add.assert_called_once_with(user_stock)
        mock_session.commit.assert_called_once()

        self.assertEqual(user_stock.stock_id, 1)
        self.assertEqual(user_stock.suma, 300.00)
        self.assertEqual(user_stock.user_id, 1)
        self.assertEqual(user_stock.company, "Test Company 3")
        self.assertEqual(user_stock.stocks_amount, 30)

        assert mock_session.commit.call_count == 1

    @patch('stocks.service.users_stocks_crud.UserStock.query')
    @patch('stocks.service.users_stocks_crud.db.session')
    def test_delete_stock(self, mock_session, mock_query):
        """Test delete_stock"""
        mock_query.filter_by.return_value.first.return_value = self.user_stock1
        delete_stock(user_id=1, stock_id=1, user_stock_id=1)
        mock_query.filter_by.assert_called_once_with(user_id=1, stock_id=1, id=1)
        mock_session.delete.assert_called_once_with(self.user_stock1)
        mock_session.commit.assert_called_once()
        assert mock_session.commit.call_count == 1
