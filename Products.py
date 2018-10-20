'''
Created on October 19, 2018

@author: Vincent Scavetta
'''
from datetime import datetime
from sqlalchemy import Column, String, PrimaryKeyConstraint, Index, ForeignKeyConstraint, Float
from sqlalchemy.dialects.mysql import SMALLINT, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from base import BASE  # Leverage an instance of the declarative_base


# the Product table
class Product(BASE):
    __tablename__ = 'product'

    product_id = Column('product_id', SMALLINT(unsigned=True), nullable=False, primary_key=True, autoincrement=True)
    name = Column('name', String(45), nullable=False)
    description = Column('description', String(45), nullable=False)
    supplier_id = Column('supplier_id', SMALLINT(unsigned=True), nullable=False)
    category_id = Column('category_id', SMALLINT(unsigned=True), nullable=False)
    cost = Column('cost', Float, nullable=False)
    reorder_level = Column('reorder_level', SMALLINT(unsigned=True), nullable=False)
    weight_unit_of_measure = Column('weight_unit_of_measure', String(3), nullable=False)
    weight = Column('weight', Float, nullable=False)
    last_update = Column('last_update', TIMESTAMP, nullable=False)

    # How to handle associated films
    #
    # Since the secondary table is also explicitly mapped elsewhere as Film_Actor
    # the relationship should have the viewonly flag so that we can save actors
    # independently of films
    ratings = relationship("customer", secondary="customer_rating", viewonly=True)
    orders = relationship("customer", secondary="customer_order", viewonly=True)
    category = relationship("category", backref=backref('product'))

    __table_args__ = (
        PrimaryKeyConstraint('product_id', name='PRIMARY'),
        ForeignKeyConstraint(['supplier_id'], ['supplier.supplier_id']),
        ForeignKeyConstraint(['category_id'], ['category.category_id']),)

    # The constructor with only the fields we care about from Product table
    def __init__(self, name, description, supplier_id, category_id, cost, reorder_level, weight_unit_of_measure, weight):
        self.name = name
        self.description = description
        self.supplier_id = supplier_id
        self.category_id = category_id
        self.cost = cost
        self.reorder_level = reorder_level
        self.weight_unit_of_measure = weight_unit_of_measure
        self.weight = weight
        self.last_update = datetime.today()

    # A __repr__ method defines how the object should be represented (like toString() in Java)
    # It typically is the constructor call required to re-create the instance.
    def __repr__(self):
        return "\nProduct(product_id = {self.product_id}, " \
               "\n\tdescription = {self.description}," \
               "\n\tdescription = {self.description}," \
               "\n\tsupplier_id = {self.supplier_id}," \
               "\n\tcategory_id = {self.category_id},"\
               "\n\tcost = {self.cost}," \
               "\n\treorder_level = {self.reorder_level}," \
               "\n\tweight_unit_of_measure = {self.weight_unit_of_measure}," \
               "\n\tweight = {self.weight}," \
               "\n\tlast_update = {self.last_update})".format(self=self)