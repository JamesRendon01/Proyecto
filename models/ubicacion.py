from db import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey, Text, VARCHAR
from sqlalchemy.orm import relationship

class Ubicacion(Base):
    __tablename__ = "ubicacion"
    id=Column(Integer, primary_key=True)
    ciudad=Column(VARCHAR(20))
    direccion=Column(VARCHAR(30))
    longitud=Column(VARCHAR(15))
    latitud=Column(VARCHAR(15))