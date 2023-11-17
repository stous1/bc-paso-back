import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.dialects.postgresql import UUID


class entites():
    def __init__(self):
        self.Base = declarative_base()
        User(self.Base)
        
    

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)    
    username = Column(String(50))
    email = Column(String(100))
    longitude = Column(Float)
    
