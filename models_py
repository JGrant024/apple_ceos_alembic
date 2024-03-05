from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import declarative_base 
from pydantic import BaseModel 

Base = declarative_base()

class CEO(Base): 
    __tablename__ = "apple_ceos"
    id = Column(Integer, primary_key=True) 
    name = Column(String)
    slug = Column(String) 
    year = Column(Integer)

class CeoSchema(BaseModel): 
    name: str
    slug: str
    year: int   

    
class Config: 
    populate_by_name = True 