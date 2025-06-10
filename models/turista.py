from db import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey, VARCHAR, Text
from sqlalchemy.orm import relationship

class Turista(Base):
    __tablename__ ="turista"
    id=Column(Integer, primary_key=True)
    nombre=Column(VARCHAR(30))
    correo=Column(VARCHAR(20))
    celular=Column(Integer)
    fecha_nacimiento=Column(Date)
    ciudad_residencia=Column(VARCHAR(20))
    direccion=Column(VARCHAR(50))
    identificacion=Column(Integer)
    contraseña=Column(VARCHAR(10))
    # id_rol=Column(Integer, ForeignKey("rol.id"))
