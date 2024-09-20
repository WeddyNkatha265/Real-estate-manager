from sqlalchemy import Column, Integer, String
from models import Base

class Buyer(Base):
    __tablename__ = 'buyers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    
    def __repr__(self):
        return f"<Buyer(name={self.name}, email={self.email})>"
