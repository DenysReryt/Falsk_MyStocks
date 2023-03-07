from flask import Flask
from flask_restful import Api
from stocks.database import sql_url
from stocks.models.models import db, migrate

app = Flask(__name__)
app.secret_key = 'Secret Key'
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = sql_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)


# # create the tables
# with stocks.app_context():
#     db.create_all()

@app.route('/')
def index():
    return 'Hello world!'


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')
