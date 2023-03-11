"""This is the main module for the MyStocks application. It sets up the Flask app and the SQLAlchemy connection to the
database, registers the API resources and blueprints, and configures logging."""
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template
from flask_restful import Api
from stocks.config import settings
from stocks.models.models import db, migrate
from stocks.rest.user_rest import UserRes, UserListRes
from stocks.rest.stock_rest import StockRes, StockListRes
from stocks.rest.users_stocks_rest import UserStockListRes, UserStockRes, UserStockDel
from stocks.views.stock_routes import stock_bp
from stocks.views.user_routes import user_bp
from stocks.views.users_stocks_routes import user_stock_bp

# Set up logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Set up logging to a file
handler = RotatingFileHandler('log/debug.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Set up logging to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# Create a Flask app instance
app = Flask(__name__)

# Set the secret key of the Flask app for sessions and cookies
app.secret_key = settings.SECRET_KEY

# Create a Flask-RESTful API instance
api = Api(app)

# Set up the SQLAlchemy connection to the database
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate.init_app(app, db)

# Add the RESTful resources to the API instance
api.add_resource(UserListRes, '/api/users')
api.add_resource(UserRes, '/api/users/<int:user_id>')
api.add_resource(UserStockListRes, '/api/users/stocks/<int:user_id>')
api.add_resource(UserStockRes, '/api/users/stocks/<int:user_id>/<int:stock_id>')
api.add_resource(UserStockDel, '/api/users/stocks/<int:user_id>/<int:stock_id>/<int:user_stock_id>')
api.add_resource(StockListRes, '/api/stocks')
api.add_resource(StockRes, '/api/stocks/<int:stock_id>')

# Register the blueprints for the views
app.register_blueprint(user_bp)
app.register_blueprint(stock_bp)
app.register_blueprint(user_stock_bp)


@app.route('/')
def home():
    """Render the home template."""
    return render_template('home.html')


if __name__ == '__main__':
    # Run the Flask app on localhost:5000
    app.run(debug=True, port=5000, host='127.0.0.1')
