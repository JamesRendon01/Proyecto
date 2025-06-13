from db import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey, Text, VARCHAR
from sqlalchemy.orm import relationship

class Hotel(Base):
    __tablename__ = "hotel"
    id=Column(Integer, primary_key=True)
    nombre=Column(String(20))
    ciudad=Column(String(20))
    direccion=Column(String(30))