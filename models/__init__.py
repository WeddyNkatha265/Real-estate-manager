# Import the declarative_base function to create a Base class
# The Base class is used to define the structure of the database tables
from sqlalchemy.ext.declarative import declarative_base

# Creating an instance of Base which will be inherited by all the models
# This Base class will manage the mappings between Python objects and database tables
Base = declarative_base()

# Importing all the models (Agent, Property, Buyer) to make them available for database creation
# This ensures that Alembic can detect the models during migrations
from .agent import Agent
from .property import Property
from .buyer import Buyer
from .buyer_property_association import buyer_property_association