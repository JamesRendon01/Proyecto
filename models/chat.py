from db import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey, VARCHAR, Text
from sqlalchemy.orm import relationship

class Chat(Base):
    __tablename__ = "chat"
    id=Column(Integer, primary_key=True)
    estado=Column(Boolean)
    mensaje=Column(VARCHAR(100))
    id_administrador=Column(Integer, ForeignKey("administrador.id"))
    id_turista=Column(Integer, ForeignKey("turista.id"))
