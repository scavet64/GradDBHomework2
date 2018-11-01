"""
Created on October 19, 2018

@author: Joseph Scavetta
"""

from datetime import datetime

from sqlalchemy import Column, String, PrimaryKeyConstraint, Index
from sqlalchemy.dialects.mysql import SMALLINT, TIMESTAMP
from sqlalchemy.orm import relationship

from base import BASE  # Leverage an instance of the declarative_base


class Customer(BASE):
    __tablename__ = 'customer'

    customer_id = Column('customer_id', SMALLINT(unsigned=True), nullable=False, primary_key=True, autoincrement=True)
    first_name = Column('first_name', String(45))
    last_name = Column('last_name', String(45), nullable=False)
    email_address = Column('email_address', String(45), nullable=False)
    last_login = Column('last_login', TIMESTAMP, nullable=False)
    last_update = Column('last_update', TIMESTAMP, nullable=False)

    ratings = relationship('product', secondary='customer_rating', viewonly=True)
    orders = relationship('product', secondary='customer_order', viewonly=True)
    shopping_cart = relationship('product', secondary='customer_shopping_cart', viewonly=True)
    wish_list = relationship('product', secondary='customer_wish_list', viewonly=True)

    address = relationship('address', secondary='customer_address', viewonly=True)

    __table_args__ = (
        PrimaryKeyConstraint('customer_id', name='PRIMARY'),
        Index('idx_customers_last_name', 'last_name'))

    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.last_login = datetime.today()
        self.last_update = datetime.today()

    def __repr__(self):
        return "\nCustomer(customer_id = {self.customer_id}, " \
               "\n\tfirst_name = {self.first_name}," \
               "\n\tlast_name = {self.last_name}," \
               "\n\temail_address = {self.email_address}," \
               "\n\tlast_login = {self.last_login}," \
               "\n\tlast_update = {self.last_update})".format(self=self)
