from sqlalchemy import Column, Integer, String
from models import Base
from db import engine
from pydantic import BaseModel

class CEO(Base):
    __tablename__ = "CEO"

    id = Column(Integer, primary_key=True)
    Name = Column(String)
    Slug = Column(String)
    Year_Served= Column(Integer)

class CEOSchema(BaseModel):
    Name: str   
    Slug: str
    Year_Served: int
    
Base.metadata.create_all(bind=engine)