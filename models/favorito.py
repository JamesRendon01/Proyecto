from db import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey, VARCHAR, Text
from sqlalchemy.orm import relationship

class Favorito(Base):
    __tablename__ = "favorito"
    id=Column(Integer, primary_key=True)
    id_turista=Column(Integer, ForeignKey("turista.id"))
    id_plan=Column(Integer, ForeignKey("plan.id"))