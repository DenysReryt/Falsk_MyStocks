"""Module with RESTful for users CRUD"""
from typing import Tuple, Dict, Union, Any, List
import json
from datetime import datetime
from sqlalchemy.exc import IntegrityError

from flask_restful import Resource
from flask import request

from stocks.service import user_crud


def json_serializer(obj) -> str:
    """
        Serialize datetime objects to ISO format.
    """
    if isinstance(obj, datetime):
        return obj.isoformat()


class UserListRes(Resource):
    """
        Resource class for listing users and creating new users.
    """

    def get(self) -> Tuple[Any, int]:
        """
            Get a list of all users.
        """
        users = user_crud.get_all_users()
        users_list = [user.to_dict() for user in users]
        json_str = json.dumps(users_list, default=json_serializer)
        return json.loads(json_str), 200

    def post(self) -> Union[Tuple[Any, int], bool]:
        """
            Create a new user.
        """
        try:
            data = request.get_json()
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            phone = data.get('phone')
            user = user_crud.create_user(first_name=first_name, last_name=last_name, phone=phone)
            json_str = json.dumps(user.to_dict(), default=json_serializer)
            return json.loads(json_str), 201
        except IntegrityError:
            return False


class UserRes(Resource):
    """
        Resource class for update get delete specific user.
    """

    def get(self, user_id: int) -> Union[Tuple[Dict[str, str], int], Tuple[List[Any], int]]:
        """
            Get a user by id.
        """
        user = user_crud.get_user(user_id=user_id)
        if not user:
            return {'message': 'User not found'}, 404
        json_str = json.dumps(user.to_dict(), default=json_serializer)
        return [json.loads(json_str)], 200

    def put(self, user_id: int) -> Union[None, Tuple[Any, int], bool]:
        """
            Update a user by id.
        """
        try:
            data = request.get_json()
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            phone = data.get('phone')
            user = user_crud.update_user(user_id=user_id, first_name=first_name, last_name=last_name, phone=phone)
            if user is None:
                return None
            json_str = json.dumps(user.to_dict(), default=json_serializer)
            return json.loads(json_str), 200
        except IntegrityError:
            return False

    def delete(self, user_id: int) -> Tuple[Dict[str, str], int]:
        """
            Delete a user.
        """
        deleted = user_crud.delete_user(user_id=user_id)
        if deleted == 0:
            return {'message': 'User not found'}, 404
        return {'message': 'Successfully deleted'}, 201
