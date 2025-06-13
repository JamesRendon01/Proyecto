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
    id_instancia=Column(Integer, ForeignKey("instancia.id"))
    id_hotel=Column(Integer, ForeignKey("hotel.id"))
    id_ruta=Column(Integer, ForeignKey("ruta.id"))