from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .agent import Agent
from .property import Property
from .buyer import Buyer
