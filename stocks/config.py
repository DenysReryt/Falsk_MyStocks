"""
Module to handle application configuration settings.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    """
        Class to define application settings.
    """

    DB_USER: str = os.getenv('DB_USER')
    DB_NAME: str = os.getenv('DB_NAME')
    DB_HOST: str = os.getenv('DB_HOST')
    SQLALCHEMY_DATABASE_URI: str = os.getenv('DB_URL')

    def __init__(self):
        pass


settings = Settings()
