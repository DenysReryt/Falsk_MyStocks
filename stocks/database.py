"""
Module to create a database URL
"""
from stocks.config import settings

sql_url = f'mysql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}/' \
          f'{settings.DB_NAME}'
