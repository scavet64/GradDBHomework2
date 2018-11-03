from flask import Flask

# create an instance of the Flask class
# Any time we run the application __name__ gets defined for the app
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import BASE
# from sakila_flask.databose_model import Film, Film_Actor, Actor, Award
from Category import Category
from Customer import Customer, CustomerWishlist
#from CustomerWishlist import CustomerWishlist
from Product import Product
connection = create_engine('mysql+pymysql://root:DATABASEPASSWORD@127.0.0.1:3306/grad_db')
# connection = create_engine('mysql+pymysql://guest:guest@localhost/guest')
BASE.metadata.create_all(connection)

Session = sessionmaker(bind=connection)
session = Session()


# Python decorators: if either of these routes get sent by the
# browser, the function listed will run.
@app.route('/')
def index():
    return "<h1>Sakila</h1><h2>Only the best movies live here</h2>"


@app.route('/Products')
def getproducts():
    product = session.query(Product).first()
    output = '<h1>' + product.name + ' ' + product.description + '</h1>'
    return output


@app.route('/Categorys')
def getfilms():
    film = session.query(Category).first()
    output = '<h1>' + film.title + '</h1>\n'
    output += '<summary>' + film.description + '</summary>\n'
    output += '<p>This film is rated ' + film.rating
    output +=  ' and was made in ' + str(film.release_year)
    output += '.  ' + film.title + ' runs for ' + str(film.length) + ' minutes.</p>\n'
    output += '<ul>\n'
    for actor in film.actors:
        output += '<li>' + actor.first_name + ' ' + actor.last_name + '</li>\n'
    return output
    output += '</ul>'


@app.route('/CustomerWishlist')
def getwishlists():
    film = session.query(CustomerWishlist).first()
    output = '<h1>' + film.title + '</h1>\n'
    output += '<summary>' + film.description + '</summary>\n'
    output += '<p>This film is rated ' + film.rating
    output +=  ' and was made in ' + str(film.release_year)
    output += '.  ' + film.title + ' runs for ' + str(film.length) + ' minutes.</p>\n'
    output += '<ul>\n'
    for actor in film.actors:
        output += '<li>' + actor.first_name + ' ' + actor.last_name + '</li>\n'
    return output
    output += '</ul>'


# # The application run by the Python interpreter gets a name 0f __main__
# if __name__ == '__main__':
#     app.debug = True
#     app.run()  # this will run the local server with this app


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
