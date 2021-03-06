from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import BASE
from Category import Category
from Customer import Customer
from Product import Product

import time

# create an instance of the Flask class
# Any time we run the application __name__ gets defined for the app
app = Flask(__name__)

started = 0;
i = 0
while i < 5 or started == 1:
    try:
        connection = create_engine('mysql+pymysql://root:PASSWORD@mysql_database:3306/grad_db')
        BASE.metadata.create_all(connection)

        Session = sessionmaker(bind=connection)
        session = Session()
        started = 1
        break
    except:
        print("Could not connect to database")
        i += 1
        time.sleep(5)


# Python decorators: if either of these routes get sent by the
# browser, the function listed will run.
@app.route('/')
def index():
    return "<h1>Amazon Silver</h1><h2>Kinda like amazon but not</h2>"


@app.route('/products')
def get_products():
    product = session.query(Product).first()
    output = '<h1>' + product.name + ' ' + product.description + '</h1>'
    return output


@app.route('/categorys')
def get_categories():
    category = session.query(Category).first()
    output = '<h1>' + category.name + '</h1>\n'
    return output


@app.route('/customer')
def get_wish_lists():
    customer = session.query(Customer).first()
    output = '<h1>' + customer.first_name + ' ' + customer.last_name + '</h1>\n'
    output += '<p>' + customer.email_address + '</p>\n'
    output += '<p>Customer Wishlist:</p>\n'
    output += '<ul>\n'
    for product in customer.wishlist:
        output += '<li>' + product.name + '</li>\n'
    return output
    output += '</ul>'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
