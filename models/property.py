from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Property(Base):
    __tablename__ = 'properties'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    agent_id = Column(Integer, ForeignKey('agents.id'))
    
    agent = relationship("Agent", back_populates="properties")
    
    def __repr__(self):
        return f"<Property(name={self.name}, price={self.price})>"
