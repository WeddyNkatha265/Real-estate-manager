# Import Column, Integer, String, ForeignKey to define the columns and relationships in the table
# Import relationship to establish relationships between tables
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Base  # Import the Base class to define the Property model

# The Property class represents the 'properties' table in the database
# It contains columns for id, name, price, and agent_id to reference the managing agent
class Property(Base):
    __tablename__ = 'properties'  # Define the table name in the database

    # Define the columns of the 'properties' table
    id = Column(Integer, primary_key=True)  # Unique identifier for each property (primary key)
    name = Column(String, nullable=False)  # Name of the property (cannot be null)
    price = Column(Integer, nullable=False)  # Price of the property (cannot be null)
    
    # ForeignKey establishes a relationship between properties and agents
    # The agent_id column links each property to the agent who manages it
    agent_id = Column(Integer, ForeignKey('agents.id'), nullable=False)
    
    # Define the relationship between Property and Agent
    # A property is "managed by" an agent, and this establishes a link back to the agent
    agent = relationship("Agent", back_populates="properties")
    
    # String representation of the Property object
    # Helps with printing and debugging property information
    def __repr__(self):
        return f"<Property(name={self.name}, price={self.price}, agent_id={self.agent_id})>"