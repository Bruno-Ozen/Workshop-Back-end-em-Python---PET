from sqlalchemy.orm import Session
from models import Petiano_BD
from schemas import PetianoBase

def cadastrar_petiano(db: Session, petiano: PetianoBase):
    """Cadastra um novo petiano"""
    petiano_db = Petiano_BD(nome=petiano.nome, email=petiano.email, cpf=petiano.email, curso=petiano.curso)
    db.add(petiano_db)
    db.commit()
    db.refresh(petiano_db)
    return petiano_db

def listar_petianos(db: Session):
    return db.query(Petiano_BD).all()

def obter_petiano(db: Session, petiano_id: int):
    return db.query(Petiano_BD).filter(Petiano_BD.id == petiano_id).first()

def deletar_petiano(db: Session, petiano_id: int):
    petiano_db = db.query(Petiano_BD).filter(Petiano_BD.id == petiano_id).first()
    if petiano_db:
        db.delete(petiano_db)
        db.commit()
    return petiano_db

def deletar_todos_petianos(db: Session):
    db.query(Petiano_BD).delete()
    db.commit()

def atualizar_petiano(db: Session, petiano_id: int, nome: str, email: str, curso: str):
    petiano_db = db.query(Petiano_BD).filter(Petiano_BD.id == petiano_id).first()
    if petiano_db:
        petiano_db.nome = nome
        petiano_db.email = email
        petiano_db.curso = curso
        db.commit()
        db.refresh(petiano_db)
    return petiano_db