"""
This script populates the database with initial data for the application.
"""

from stocks.models.models import db, User, Stock

# create some users
user1 = User(first_name='Denys', last_name='Radchenko', phone='380500000000')
user2 = User(first_name='Petro', last_name='Yavir', phone='380970000000')

# add the users to the session
db.session.add(user1)
db.session.add(user2)

# create some stocks
stock1 = Stock(company='Apple Inc.', sector='Technology', amount=100, price=1500.0)
stock2 = Stock(company='Ford Motor Company', sector='Automotive', amount=500, price=25.0)

# add the stocks to the session
db.session.add(stock1)
db.session.add(stock2)

# commit the changes to the database
db.session.commit()
