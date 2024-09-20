# Import Column, Integer, String for defining columns in the database table
# Import relationship to set up relationships between tables
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import Base  # Import the Base class to define the Agent model

# The Agent class represents the 'agents' table in the database
# It contains columns for id, name, and phone of the agent
class Agent(Base):
    __tablename__ = 'agents'  # Define the table name in the database
    
    # Define the columns of the agents table
    id = Column(Integer, primary_key=True)  # Unique identifier for each agent (primary key)
    name = Column(String, nullable=False)  # Name of the agent (cannot be null)
    phone = Column(String, nullable=False)  # Phone number of the agent (cannot be null)

    # Relationship to the Property class (one-to-many relationship)
    # One agent can manage multiple properties
    properties = relationship("Property", back_populates="agent")
    
    # String representation of the Agent object
    # Useful when printing or debugging agent information
    def __repr__(self):
        return f"<Agent(name={self.name}, phone={self.phone})>"
