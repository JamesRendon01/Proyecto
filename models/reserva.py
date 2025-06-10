from db import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey, VARCHAR, Text
from sqlalchemy.orm import relationship

class Reserva(Base):
    __tablename__ = "reserva"
    id=Column(Integer, primary_key=True)
    fecha_inicio=Column(Date)
    fecha_fin=Column(Date)
    precio=Column(Integer)
    id_turista=Column(Integer, ForeignKey("turista.id"))