'''
Created on October 19, 2018

@author: Vincent Scavetta
'''
from datetime import datetime
from sqlalchemy import Column, String, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.orm import relationship
from base import BASE  # Leverage an instance of the declarative_base


# one category can have many products
class Category(BASE):
    __tablename__ = 'category'

    category_id = Column('category_id', SMALLINT(unsigned=True), nullable=False, primary_key=True)
    name = Column('name', String(255), nullable=False)

    products = relationship("product", viewonly=True)

    __table_args__ = (
        PrimaryKeyConstraint('category_id', name='PRIMARY'),)

    # The constructor
    #   Note: Different from the flack constructor, as we will pass actor not actor_ids
    def __init__(self, name, products=None):
        self.name = name
        self.products = products
