import unittest
from unittest.mock import patch
from stocks.rest.user_rest import UserListRes, UserRes
from stocks.models.models import User
from stocks.main import app
import datetime

registration_date = datetime.datetime.now()


class TestUserListRes(unittest.TestCase):

    @patch('stocks.rest.user_rest.user_crud.get_all_users')
    def test_get_returns_users_as_json(self, mock_get_all_users):
        mock_user1 = User(id=1, first_name='John', last_name='Doe', stocks_amount=0,
                          registration_date=str(registration_date), phone='1234567890')
        mock_user2 = User(id=2, first_name='Jane', last_name='Doe', stocks_amount=0,
                          registration_date=str(registration_date), phone='0987654321')
        mock_get_all_users.return_value = [mock_user1, mock_user2]

        response, status_code = UserListRes().get()

        expected_json = [
            {
                'id': 1,
                'first_name': 'John',
                'last_name': 'Doe',
                "stocks_amount": 0,
                "registration_date": str(registration_date),
                'phone': '1234567890',
            },
            {
                'id': 2,
                'first_name': 'Jane',
                'last_name': 'Doe',
                "stocks_amount": 0,
                "registration_date": str(registration_date),
                'phone': '0987654321',
            },
        ]
        self.assertEqual(response, expected_json)
        self.assertEqual(status_code, 200)

    @patch('stocks.rest.user_rest.user_crud.create_user')
    def test_post_creates_new_user(self, mock_create_user):
        with app.test_request_context(json={'first_name': 'John', 'last_name': 'Doe', 'phone': '1234567890'}):
            mock_user = User(id=1, first_name='John', last_name='Doe', stocks_amount=0,
                             registration_date=str(registration_date), phone='1234567890')
            mock_create_user.return_value = mock_user

            response, status_code = UserListRes().post()

            expected_json = {
                'id': 1,
                'first_name': 'John',
                'last_name': 'Doe',
                "stocks_amount": 0,
                "registration_date": str(registration_date),
                'phone': '1234567890',
            }
            self.assertEqual(response, expected_json)
            self.assertEqual(status_code, 201)

class TestUserRes(unittest.TestCase):
    @patch('stocks.rest.user_rest.user_crud.get_user')
    def test_get_returns_user_as_json(self, mock_get_user):
        mock_user = User(id=1, first_name='John', last_name='Doe', stocks_amount=0,
                         registration_date=str(registration_date), phone='1234567890')
        mock_get_user.return_value = mock_user

        response, status_code = UserRes().get(1)

        expected_json = [{
            'id': 1,
            'first_name': 'John',
            'last_name': 'Doe',
            "stocks_amount": 0,
            "registration_date": str(registration_date),
            'phone': '1234567890',
        }
        ]
        self.assertEqual(response, expected_json)
        self.assertEqual(status_code, 200)

    @patch('stocks.rest.user_rest.user_crud.update_user')
    def test_put_updates_existing_user(self, mock_update_user):
        with app.test_request_context(json={'first_name': 'John', 'last_name': 'Doe', 'phone': '1234567890'}):
            mock_user = User(id=1, first_name='John', last_name='Doe', stocks_amount=0,
                             registration_date=str(registration_date), phone='1234567890')
            mock_update_user.return_value = mock_user

            response, status_code = UserRes().put(1)

            expected_json = {
                    'id': 1,
                    'first_name': 'John',
                    'last_name': 'Doe',
                    "stocks_amount": 0,
                    "registration_date": str(registration_date),
                    'phone': '1234567890',
                }
            self.assertEqual(response, expected_json)
            self.assertEqual(status_code, 200)

    @patch('stocks.rest.user_rest.user_crud.delete_user')
    def test_delete_existing_user(self, mock_delete_user):
        response, status_code = UserRes().delete(1)
        self.assertEqual(response, {'message': 'Successfully deleted'})
        self.assertEqual(status_code, 204)
