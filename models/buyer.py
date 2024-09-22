# Import necessary SQLAlchemy components
# Column, Integer, String for defining the database columns
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import Base
from models.buyer_property_association import buyer_property_association  # Import the Base class to define the Buyer model

# The Buyer class represents the 'buyers' table in the database
# It stores information about people interested in buying properties
class Buyer(Base):
    __tablename__ = 'buyers'  # Define the table name in the database

    # Define the columns of the 'buyers' table
    id = Column(Integer, primary_key=True)  # Unique identifier for each buyer (primary key)
    name = Column(String, nullable=False)  # Name of the buyer (cannot be null)
    email = Column(String, nullable=False)  # Email address of the buyer (cannot be null)

    # Establish a many-to-many relationship with the Property class
    interested_properties = relationship(
        "Property",
        secondary=buyer_property_association,  # Use the association table
        back_populates="interested_buyers"  # Link back to Property
    )

    # String representation of the Buyer object
    # Useful for printing or debugging buyer information
    def __repr__(self):
        return f"<Buyer(name={self.name}, email={self.email})>"
