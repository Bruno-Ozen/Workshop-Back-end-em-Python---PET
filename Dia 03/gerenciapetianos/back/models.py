from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Petiano_BD(Base):
    """Modelo de petianos para o banco de dados"""
    __tablename__ = "petianos"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String, unique=True)
    email = Column(String, unique=True)
    curso = Column(String)
