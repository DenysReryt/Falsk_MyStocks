import unittest
from unittest.mock import patch, MagicMock

from stocks.main import app
from stocks.config import settings
from stocks.models.models import User
from stocks.service.user_crud import create_user, delete_user, get_all_users, get_user, update_user


class TestUserCrud(unittest.TestCase):
    def setUp(self):
        self.user1 = User(id=1, first_name='John', last_name='Doe', stocks_amount=10, phone='1234567890')
        self.user2 = User(id=2, first_name='Jane', last_name='Doe', stocks_amount=20, phone='0987654321')

        # Set up the Flask application context
        app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
        app.config['TESTING'] = True
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        # Remove the Flask application context
        self.app_context.pop()

    @patch('stocks.service.user_crud.User.query')
    def test_get_all_users(self, mock_query):
        mock_query.all.return_value = [self.user1, self.user2]

        users = get_all_users()

        mock_query.all.assert_called_once()
        self.assertEqual(len(users), 2)
        self.assertIn(self.user1, users)
        self.assertIn(self.user2, users)

    @patch('stocks.service.user_crud.User.query')
    def test_get_user(self, mock_query):
        # Set up mock data
        mock_query.filter_by.return_value.first.return_value = self.user1

        # Call the function
        user = get_user(1)

        # Assert the expected results
        mock_query.filter_by.assert_called_once_with(id=1)
        mock_query.filter_by.return_value.first.assert_called_once()
        self.assertEqual(user, self.user1)

    @patch('stocks.service.user_crud.db')
    def test_create_user(self, mock_db):
        mock_db.session.add.return_value = MagicMock()
        mock_db.session.commit.return_value = None

        user = create_user('Bob', 'Smith', '5555555555')

        mock_db.session.add.assert_called_once()
        mock_db.session.commit.assert_called_once()
        self.assertEqual(user.first_name, 'Bob')
        self.assertEqual(user.last_name, 'Smith')
        self.assertEqual(user.phone, '5555555555')


    @patch('stocks.service.user_crud.db')
    def test_update_user(self, mock_db):
        # Create a mock user object to be returned by the query
        mock_user = MagicMock()
        mock_db.session.query.return_value.filter_by.return_value.first.return_value = mock_user

        # Call the function to update the user
        updated_user = update_user(user_id=1, first_name='John', last_name='Doe', phone='1234567890')

        # Assert that the query was called with the correct arguments
        mock_db.session.query.assert_called_once_with(User)
        mock_db.session.query.return_value.filter_by.assert_called_once_with(id=1)
        mock_db.session.query.return_value.filter_by.return_value.first.assert_called_once()

        # Assert that the user object was updated with the new values
        mock_user.first_name.assert_called_once_with('John')
        mock_user.last_name.assert_called_once_with('Doe')
        mock_user.phone.assert_called_once_with('1234567890')

        # Assert that the session was committed
        mock_db.session.commit.assert_called_once()

        # Assert that the updated user object was returned
        self.assertEqual(updated_user, mock_user)
    # def test_update_user(self, mock_session):
    #     # Create a mock User object
    #     mock_user = User(id=1, first_name='John', last_name='Doe', phone='1234567890')
    #
    #     # Set up the mock session to return the mock User object when queried
    #     mock_session.query.return_value.filter_by.return_value.first.return_value = mock_user
    #
    #     # Call the update_user function with some new values
    #     updated_user = update_user(1, first_name='Bob', last_name='Doe', phone='5555555555')
    #     mock_session.commit()
    #
    #     # Assert that the mock session's commit method was called once
    #     mock_session.commit.assert_called_once()
    #     self.assertIsNotNone(User.query.filter_by(id=1).first())
    #     # Assert that the returned User object has the expected values
    #     self.assertEqual(updated_user.id, 1)
    #     self.assertEqual(updated_user.first_name, 'Bob')
    #     self.assertEqual(updated_user.last_name, 'Doe')
    #     self.assertEqual(updated_user.phone, '5555555555')


    @patch('stocks.service.user_crud.User.query')
    @patch('stocks.service.user_crud.db.session')
    def test_delete_user(self, mock_session, mock_user_query):
        # Set up mock user object
        user = MagicMock()
        user.id = 1
        mock_user_query.filter_by.return_value.first.return_value = user

        # Call delete_user function
        result = delete_user(1)

        # Check that session was used to delete user
        mock_session.delete.assert_called_once_with(user)

        # Check that session was committed
        mock_session.commit.assert_called_once()

        # Check that result is True
        self.assertEqual(result, None)

        # Check case where user does not exist
        mock_user_query.filter_by.return_value.first.return_value = None
        result = delete_user(1)
        self.assertEqual(result, False)
