import unittest, json
from unittest.mock import patch, MagicMock
from stocks.rest.stock_rest import StockRes, StockListRes
from stocks.models.models import Stock
from stocks.main import app


class TestStockListRes(unittest.TestCase):

    @patch('stocks.rest.stock_rest.stock_crud.get_all_stocks')
    def test_get_returns_stocks_as_json(self, mock_get_all_stocks):
        mock_stock1 = Stock(id=1, company='Amazon', sector='Technology', amount=1000, price=35.55)
        mock_stock2 = Stock(id=2, company='Microsoft', sector='Technology', amount=500, price=173.12)

        mock_get_all_stocks.return_value = [mock_stock1, mock_stock2]

        response, status_code = StockListRes().get()

        expected_json = [
            {
                'id': 1,
                'company': 'Amazon',
                'sector': 'Technology',
                "amount": 1000,
                "price": 35.55
            },
            {
                'id': 2,
                'company': 'Microsoft',
                'sector': 'Technology',
                "amount": 500,
                "price": 173.12
            },
        ]
        self.assertEqual(response, expected_json)
        self.assertEqual(status_code, 200)

    @patch('stocks.rest.stock_rest.stock_crud.create_stock')
    def test_post_creates_new_stock(self, mock_create_stock):
        with app.test_request_context(json={'company': 'Amazon', 'sector': 'Technology', 'amount': 1000,
                                            'price': 173.12}):
            mock_stock = Stock(id=1, company='Amazon', sector='Technology', amount=1000, price=35.55)
            mock_create_stock.return_value = mock_stock

            response, status_code = StockListRes().post()

            expected_json = {
                'id': 1,
                'company': 'Amazon',
                'sector': 'Technology',
                "amount": 1000,
                "price": 35.55
            }
            self.assertEqual(response, expected_json)
            self.assertEqual(status_code, 201)


class TestStockRes(unittest.TestCase):
    @patch('stocks.rest.stock_rest.stock_crud.get_stock')
    def test_get_returns_stock_as_json(self, mock_get_stock):
        mock_stock = Stock(id=1, company='Amazon', sector='Technology', amount=1000, price=35.55)
        mock_get_stock.return_value = mock_stock

        response, status_code = StockRes().get(1)

        expected_json = {
            'id': 1,
            'company': 'Amazon',
            'sector': 'Technology',
            "amount": 1000,
            "price": 35.55
        }
        self.assertEqual(response, expected_json)
        self.assertEqual(status_code, 200)


    @patch('stocks.rest.stock_rest.stock_crud.update_stock')
    def test_put_updates_existing_stock(self, mock_update_stock):
        with app.test_request_context(
                json={'company': 'Amazon', 'amount': 1000, 'price': 173.12}):
            mock_stock = Stock(id=1, company='Amazon', sector='Technology', amount=1000, price=35.55)
            mock_update_stock.return_value = mock_stock

            response, status_code = StockRes().put(stock_id=1)

            expected_json = {
                'message': 'Stock not found',
                'id': 1,
                'company': 'Amazon',
                'sector': 'Technology',
                "amount": 1000,
                "price": 35.55
            }

            self.assertEqual(response, expected_json)
            self.assertEqual(status_code, 200)

    @patch('stocks.rest.stock_rest.stock_crud.delete_stock')
    def test_delete_existing_stock(self, mock_delete_stock):
        response, status_code = StockRes().delete(1)
        self.assertEqual(response, {'message': 'Successfully deleted'})
        self.assertEqual(status_code, 201)
