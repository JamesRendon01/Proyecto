from db import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey, Text, VARCHAR, DateTime
from sqlalchemy.orm import relationship

class Ruta(Base):
    __tablename__ = "ruta"
    id=Column(Integer, primary_key=True)
    distancia=Column(String(20))
    ciudad=Column(DateTime)