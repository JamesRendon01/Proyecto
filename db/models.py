from .database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey, VARCHAR, Text
from sqlalchemy.orm import relationship

class Turista(Base):
    __tablename__ ="turista"
    id=Column(Integer, primary_key=True)
    nombre=Column(VARCHAR(30))
    correo=Column(VARCHAR(20))
    contraseña=Column(VARCHAR(10))
    celular=Column(Integer)

class Usuario(Base):
    __tablename__ = "usuario"
    id=Column(Integer, primary_key=True)
    nombre=Column(VARCHAR(30))
    correo=Column(VARCHAR(20))
    contraseña=Column(VARCHAR(30))
    celular=Column(Integer)
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

class Novedades(Base):
    __tablename__ = "novedades"
    id=Column(Integer, primary_key=True)
    titulo=Column(VARCHAR(50))
    descripcion=Column(VARCHAR(50))
    fecha_publicacion=Column(Date)
    imagen=Column(Text())

class Chat(Base):
    __tablename__ = "chat"
    id=Column(Integer, primary_key=True)
    estado=Column(Boolean)
    fecha_envio=Column(Date)
    id_usuario=Column(Integer, ForeignKey("usuario.id"))
    id_turista=Column(Integer, ForeignKey("turista.id"))

class Mensajes(Base):
    __tablename__ = "mensajes"
    id=Column(Integer, primary_key=True)
    remitente=Column(VARCHAR(50))
    mensaje=Column(VARCHAR(100))
    fecha_envio=Column(Date)
    id_chat=Column(Integer, ForeignKey("chat.id"))

class Informes(Base):
    __tablename__ = "informes"
    id=Column(Integer, primary_key=True)
    fecha_creacion=Column(Date)
    hora_descripcion=Column(Date)
    id_usuario=Column(Integer, ForeignKey("usuario.id"))

class Horario(Base):
    __tablename__ = "horario"
    id=Column(Integer, primary_key=True)
    fecha=Column(Date)
    estado=Column(Boolean)
    id_plan=Column(Integer, ForeignKey("plan.id"))

class Notificaciones(Base):
    __tablename__ = "notificaciones"
    id=Column(Integer, primary_key=True)
    mensaje=Column(VARCHAR(50))
    id_usuario=Column(Integer, ForeignKey("usuario.id"))
    id_chat=Column(Integer, ForeignKey("chat.id"))