import unittest
from unittest.mock import patch, MagicMock
from stocks.rest.users_stocks_rest import UserStockDel, UserStockRes, UserStockListRes
from stocks.main import app


class TestUserStockListRes(unittest.TestCase):
    @patch('stocks.rest.users_stocks_rest.users_stocks_crud.get_all_user_stocks')
    def test_get(self, mock_get_all_user_stocks):
        mock_get_all_user_stocks.return_value = [MagicMock(
            to_dict=lambda: {'id': 1, 'user_id': 1, 'stock_id': 1, 'company': 'AAPL', 'stocks_amount': 10,
                             'suma': 100.00})]

        response, status_code = UserStockListRes().get(user_id=1)

        self.assertEqual(status_code, 200)
        self.assertIsInstance(response, list)
        self.assertDictEqual(response[0], {'id': 1, 'user_id': 1, 'stock_id': 1, 'company': 'AAPL', 'stocks_amount': 10,
                                           'suma': 100.00})

    @patch('stocks.rest.users_stocks_rest.users_stocks_crud.create_user_stock')
    @patch('stocks.rest.users_stocks_rest.stock_crud.get_stock_by_company')
    @patch('stocks.rest.users_stocks_rest.stock_crud.update_stock')
    def test_post(self, mock_update_stock, mock_get_stock_by_company, mock_create_user_stock):
        with app.test_request_context(json={'company': 'AAPL', 'stocks_amount': 10}):
            mock_create_user_stock.return_value = MagicMock(
                to_dict=lambda: {'id': 1, 'user_id': 1, 'stock_id': 1, 'company': 'AAPL', 'stocks_amount': 10,
                                 'suma': 100.00})
            mock_get_stock_by_company.return_value = MagicMock(
                amount=100, price=10.0)
            mock_update_stock.return_value = None

            response, status_code = UserStockListRes().post(user_id=1)

            self.assertEqual(status_code, 201)
            self.assertIsInstance(response, dict)
            self.assertDictEqual(response, {'id': 1, 'user_id': 1, 'stock_id': 1, 'company': 'AAPL', 'stocks_amount': 10,
                                            'suma': 100.00})



class TestUserStockRes(unittest.TestCase):
    @patch('stocks.rest.users_stocks_rest.users_stocks_crud.get_user_stock')
    def test_get(self, mock_get_user_stock):
        mock_get_user_stock.return_value = [MagicMock(
            to_dict=lambda: {'id': 1, 'user_id': 1, 'stock_id': 1, 'company': 'AAPL', 'stocks_amount': 10,
                             'suma': 100.00})]

        response, status_code = UserStockRes().get(user_id=1, stock_id=1)

        self.assertEqual(status_code, 200)
        self.assertIsInstance(response, list)
        self.assertDictEqual(response[0], {'id': 1, 'user_id': 1, 'stock_id': 1, 'company': 'AAPL', 'stocks_amount': 10,
                                           'suma': 100.00})


class TestUserStockDel(unittest.TestCase):
    @patch('stocks.rest.users_stocks_rest.users_stocks_crud.delete_stock')
    def test_delete(self, mock_delete_stock):
        mock_delete_stock.return_value = True

        response, status_code = UserStockDel().delete(user_id=1, stock_id=1, user_stock_id=1)

        self.assertEqual(status_code, 201)
        self.assertDictEqual(response, {'message': 'Successfully deleted'})

    @patch('stocks.rest.users_stocks_rest.users_stocks_crud.delete_stock')
    def test_delete_not_found(self, mock_delete_stock):
        mock_delete_stock.return_value = False

        response, status_code = UserStockDel().delete(user_id=1, stock_id=1, user_stock_id=1)

        self.assertEqual(status_code, 404)
        self.assertDictEqual(response, {'message': 'Stock not found'})
