"""Installation file telling Python how to install this project."""
from setuptools import setup, find_packages

setup(
    name='MyStocks',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        "flask==2.2.3",
        "gunicorn==20.1.0",
        "flask-sqlalchemy==3.0.3",
        "flask-migrate==4.0.4",
        "python-dotenv==1.0.0",
        "flask-restful==0.3.9",
        "flask-mysqldb==1.0.1",
        "coverage==7.2.1",
        "requests==2.28.2"
    ],
    entry_points={
        'console_scripts': [
            'mystocks = stocks.main:app'
        ]
    },
)
