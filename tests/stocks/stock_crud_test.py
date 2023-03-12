import unittest
from unittest.mock import patch, MagicMock

from stocks.main import app
from stocks.config import settings
from stocks.models.models import Stock
from stocks.service.stock_crud import create_stock, delete_stock, update_stock, get_stock, get_all_stocks, \
    get_stock_by_company


class TestStockCrud(unittest.TestCase):
    def setUp(self):
        self.stock1 = Stock(id=1, company='Amazon', sector='Technology', amount=1000, price=35.55)
        self.stock2 = Stock(id=2, company='Microsoft', sector='Technology', amount=500, price=173.12)

        # Set up the Flask application context
        app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
        app.config['TESTING'] = True
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        # Remove the Flask application context
        self.app_context.pop()

    @patch('stocks.service.stock_crud.Stock.query')
    def test_get_all_stocks(self, mock_query):
        mock_query.all.return_value = [self.stock1, self.stock2]

        stocks = get_all_stocks()

        mock_query.all.assert_called_once()
        self.assertEqual(len(stocks), 2)
        self.assertIn(self.stock1, stocks)
        self.assertIn(self.stock2, stocks)

    @patch('stocks.service.stock_crud.Stock.query')
    def test_get_stock(self, mock_query):
        # Set up mock data
        mock_query.filter_by.return_value.first.return_value = self.stock1

        # Call the function
        stock = get_stock(1)

        # Assert the expected results
        mock_query.filter_by.assert_called_once_with(id=1)
        mock_query.filter_by.return_value.first.assert_called_once()
        self.assertEqual(stock, self.stock1)

    @patch('stocks.service.stock_crud.Stock.query')
    def test_get_stock_by_company(self, mock_query):
        mock_query.filter_by.return_value.first.return_value = self.stock1
        stock = get_stock_by_company('Amazon')
        mock_query.filter_by.assert_called_once_with(company='Amazon')
        mock_query.filter_by.return_value.first.assert_called_once()
        self.assertEqual(stock.id, self.stock1.id)
        self.assertEqual(stock.company, self.stock1.company)
        self.assertEqual(stock.sector, self.stock1.sector)
        self.assertEqual(stock.amount, self.stock1.amount)
        self.assertEqual(stock.price, self.stock1.price)

    @patch('stocks.service.stock_crud.db')
    def test_create_stock(self, mock_db):
        mock_db.session.add.return_value = MagicMock()
        mock_db.session.commit.return_value = None

        stock = create_stock('Apple Inc.', 'Technology', 2000, 154.79)

        mock_db.session.add.assert_called_once()
        mock_db.session.commit.assert_called_once()
        self.assertEqual(stock.company, 'Apple Inc.')
        self.assertEqual(stock.sector, 'Technology')
        self.assertEqual(stock.amount, 2000)
        self.assertEqual(stock.price, 154.79)

    @patch('stocks.service.stock_crud.db')
    @patch('stocks.service.stock_crud.UserStock.query')
    def test_update_stock(self, mock_user_stock_query, mock_db):
        mock_stock = MagicMock(
            to_dict=lambda: {'id': 1, 'company': 'Amazon', 'sector': 'Technology', 'amount': 1000,
                             'price': 35.55})

        mock_db.session.query.return_value.filter_by.return_value.first.return_value = mock_stock
        mock_user_stock_query.filter_by.return_value.all.return_value = [MagicMock(stocks_amount=20)]

        with mock_db.session.begin(subtransactions=True):
            updated_stock = update_stock(1, amount=100, price=50)
            for user_stock in mock_user_stock_query.filter_by.return_value.all.return_value:
                k = int(user_stock.stocks_amount) * 50
                user_stock.suma = round(k, 2)

        mock_db.session.commit.assert_called_once()
        self.assertEqual(updated_stock.amount, 100)
        self.assertEqual(updated_stock.price, 50)
        for user_stock in mock_user_stock_query.filter_by.return_value.all.return_value:
            k = int(user_stock.stocks_amount) * 50
            self.assertEqual(user_stock.suma, round(k, 2))

    @patch('stocks.service.stock_crud.Stock.query')
    @patch('stocks.service.stock_crud.db.session')
    def test_delete_stock(self, mock_session, mock_stock_query):
        stock = MagicMock()
        stock.id = 1
        mock_stock_query.filter_by.return_value.first.return_value = stock
        result = delete_stock(1)

        mock_session.delete.assert_called_once_with(stock)
        mock_session.commit.assert_called_once()
        self.assertEqual(result, None)

        mock_stock_query.filter_by.return_value.first.return_value = None
        result = delete_stock(1)
        self.assertEqual(result, False)
