from db import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey, VARCHAR, Text
from sqlalchemy.orm import relationship

class Informe(Base):
    __tablename__ = "informe"
    id=Column(Integer, primary_key=True)
    fecha_creacion=Column(Date)
    id_administrador=Column(Integer, ForeignKey("administrador.id"))