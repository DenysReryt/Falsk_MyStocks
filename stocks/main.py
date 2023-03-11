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
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.secret_key = settings.SECRET_KEY
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

api.add_resource(UserListRes, '/api/users')
api.add_resource(UserRes, '/api/users/<int:user_id>')
api.add_resource(UserStockListRes, '/api/users/stocks/<int:user_id>')
api.add_resource(UserStockRes, '/api/users/stocks/<int:user_id>/<int:stock_id>')
api.add_resource(UserStockDel, '/api/users/stocks/<int:user_id>/<int:stock_id>/<int:user_stock_id>')
api.add_resource(StockListRes, '/api/stocks')
api.add_resource(StockRes, '/api/stocks/<int:stock_id>')

app.register_blueprint(user_bp)
app.register_blueprint(stock_bp)
app.register_blueprint(user_stock_bp)

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


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')
