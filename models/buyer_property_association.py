from sqlalchemy import Table, Column, Integer, ForeignKey
from models import Base

# Define the association table to link buyers and properties (Many-to-Many)
buyer_property_association = Table(
    'buyer_property_association', Base.metadata,
    Column('buyer_id', Integer, ForeignKey('buyers.id'), primary_key=True),  # Link to buyer
    Column('property_id', Integer, ForeignKey('properties.id'), primary_key=True)  # Link to property
)
