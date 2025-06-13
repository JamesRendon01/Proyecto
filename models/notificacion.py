from db import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey, VARCHAR, Text
from sqlalchemy.orm import relationship

class Notificacion(Base):
    __tablename__ = "notificacion"
    id=Column(Integer, primary_key=True)
    mensaje=Column(VARCHAR(50))
    id_administrador=Column(Integer, ForeignKey("administrador.id"))
    id_chat=Column(Integer, ForeignKey("chat.id"))