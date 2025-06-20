from .database import Base
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
    id_rol=Column(Integer, ForeignKey("rol.id"))

class Administrador(Base):
    __tablename__ = "administrador"
    id=Column(Integer, primary_key=True)
    nombre=Column(VARCHAR(30))
    correo=Column(VARCHAR(20))
    celular=Column(Integer)
    identificacion=Column(Integer)
    contraseña=Column(VARCHAR(10))
    id_rol=Column(Integer, ForeignKey("rol.id"))

class Rol(Base):
    __tablename__ = "rol"
    id=Column(Integer, primary_key=True)
    nombre=Column(VARCHAR(20))

class Plan(Base):
    __tablename__ = "plan"
    id=Column(Integer, primary_key=True)
    nombre=Column(VARCHAR(30))
    ubicacion=Column(VARCHAR(50))
    descripcion=Column(VARCHAR(100))
    numero_dias=Column(Integer)
    numero_noches=Column(Integer)
    horario=Column(Date)

class Reserva(Base):
    __tablename__ = "reserva"
    id=Column(Integer, primary_key=True)
    fecha_inicio=Column(Date)
    fecha_fin=Column(Date)
    precio=Column(Integer)
    id_turista=Column(Integer, ForeignKey("turista.id"))
    id_plan=Column(Integer, ForeignKey("plan.id"))

class Favoritos(Base):
    __tablename__ = "favoritos"
    id=Column(Integer, primary_key=True)
    id_turista=Column(Integer, ForeignKey("turista.id"))
    id_plan=Column(Integer, ForeignKey("plan.id"))

class Chat(Base):
    __tablename__ = "chat"
    id=Column(Integer, primary_key=True)
    estado=Column(Boolean)
    mensaje=Column(VARCHAR(100))
    id_administrador=Column(Integer, ForeignKey("administrador.id"))
    id_turista=Column(Integer, ForeignKey("turista.id"))

class Informes(Base):
    __tablename__ = "informes"
    id=Column(Integer, primary_key=True)
    fecha_creacion=Column(Date)
    id_administrador=Column(Integer, ForeignKey("administrador.id"))

class Notificaciones(Base):
    __tablename__ = "notificaciones"
    id=Column(Integer, primary_key=True)
    mensaje=Column(VARCHAR(50))
    id_administrador=Column(Integer, ForeignKey("administrador.id"))
    id_chat=Column(Integer, ForeignKey("chat.id"))