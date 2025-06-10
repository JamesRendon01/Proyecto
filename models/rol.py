from db import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey, VARCHAR, Text
from sqlalchemy.orm import relationship


class Rol(Base):
    __tablename__ = "rol"
    id=Column(Integer, primary_key=True)
    nombre=Column(VARCHAR(20))