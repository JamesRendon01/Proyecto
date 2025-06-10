from db import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey, VARCHAR, Text
from sqlalchemy.orm import relationship

class Plan(Base):
    __tablename__ = "plan"
    id=Column(Integer, primary_key=True)
    nombre=Column(VARCHAR(30))
    ubicacion=Column(VARCHAR(50))
    descripcion=Column(VARCHAR(100))
    numero_dias=Column(Integer)
    numero_noches=Column(Integer)
    horario=Column(Date)