from db import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey, VARCHAR, Text
from sqlalchemy.orm import relationship

class Instancia(Base):
    __tablename__ = "instancia"
    id=Column(Integer, primary_key=True)
    fecha_inicio=Column(Date)
    fecha_fin=Column(Date)
    costo=Column(Integer)
    id_plan=Column(Integer, ForeignKey("plan.id"))