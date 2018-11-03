# """
# Created on October 31, 2018
#
# @author: Joseph Scavetta
# """
#
# import datetime
#
# from sqlalchemy import Column, ForeignKey, PrimaryKeyConstraint, ForeignKeyConstraint
# from sqlalchemy.dialects.mysql import SMALLINT, TIMESTAMP
# from sqlalchemy.orm import relationship, backref
#
# from base import BASE
#
#
# class CustomerWishlist(BASE):
#     __tablename__ = 'customer_wishlist'
#
#     customer_id = Column('customer_id', SMALLINT(unsigned=True), ForeignKey('customer.customer_id'), nullable=False)
#     product_id = Column('product_id', SMALLINT(unsigned=True), ForeignKey('product.product_id'), nullable=False)
#     last_update = Column('last_update', TIMESTAMP, nullable=False)
#
#     customers = relationship('Customer', backref=backref('customer_wishlist'))
#     products = relationship('Product', backref=backref('customer_wishlist'))
#
#     __table_args__ = (
#         PrimaryKeyConstraint('customer_id', 'product_id', name='PRIMARY'),
#         ForeignKeyConstraint(['customer_id'], ['customer.customer_id']),
#         ForeignKeyConstraint(['product_id'], ['product.product_id']))
#
#     def __init__(self, customer, product):
#         self.customer = customer
#         self.product = product
#         self.last_update = datetime.today()
