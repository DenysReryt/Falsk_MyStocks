"""Module for CRUD operations to work with stocks table"""
from typing import List, Optional
from stocks.models.models import db, User


def get_all_users() -> List[User]:
    """Retrieve a list of all Users in the database."""
    query = User.query
    return query.all()


def get_user(user_id: int) -> Optional[User]:
    """Retrieve a specific User by ID."""
    return User.query.filter_by(id=user_id).first()


def create_user(first_name: str, last_name: str, phone: str) -> User:
    """ Create a new User."""
    user = User(first_name=first_name, last_name=last_name, phone=phone)
    db.session.add(user)
    db.session.commit()
    return user


def update_user(user_id: int, first_name: Optional[str] = None, last_name: Optional[str] = None,
                phone: Optional[str] = None) -> Optional[User]:
    """Update an existing User."""
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return None
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    if phone:
        user.phone = phone
    db.session.commit()
    return user


def delete_user(user_id: int) -> int:
    """Delete an existing User."""
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return 0
    db.session.delete(user)
    db.session.commit()
