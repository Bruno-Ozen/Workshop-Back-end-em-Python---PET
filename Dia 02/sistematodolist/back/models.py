from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True)
    descricao = Column(String)
    dono_id = Column(Integer, ForeignKey("usuarios.id"))

    dono = relationship("Usuario", back_populates="tarefas")

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    senha_hashed = Column(String)

    tarefas = relationship("Tarefa", back_populates="dono", cascade="all, delete-orphan")