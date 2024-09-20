from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import Base

class Agent(Base):
    __tablename__ = 'agents'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    
    properties = relationship("Property", back_populates="agent")
    
    def __repr__(self):
        return f"<Agent(name={self.name}, phone={self.phone})>"
