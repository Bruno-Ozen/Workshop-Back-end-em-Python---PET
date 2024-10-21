from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from models import Base
from database import engine, SessaoLocal
import schemas, crud

# Cria as tabelas do banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configuração do CORS para permitir requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    """Obtém uma sessão de banco de dados para cada requisição."""
    db = SessaoLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/petianos", response_model=schemas.Petiano)
def cadastrar_petiano(petiano: schemas.PetianoBase, db: Session = Depends(get_db)):
    """Rota para cadastrar um novo petiano."""
    return crud.cadastrar_petiano(db, petiano)

@app.get("/petianos", response_model=List[schemas.Petiano])
def listar_petianos(db: Session = Depends(get_db)):
    """Rota para listar todos os petianos"""
    return crud.listar_petianos(db)

@app.get("/petianos/{id}", response_model=schemas.Petiano)
def obter_petiano(id: int, db: Session = Depends(get_db)):
    """Rota para obter um petiano específico"""
    return crud.obter_petiano(db, id)

@app.put("/petianos/{id}", response_model=schemas.Petiano)
def atualizar_petiano(id: int, petiano: schemas.PetianoBase, db: Session = Depends(get_db)):
    """Rota para atualizar um petiano"""
    petiano_atualizado = crud.atualizar_petiano(db, id, petiano.nome, petiano.email, petiano.curso)
    if petiano_atualizado is None:
        raise HTTPException(status_code=404, detail="Petiano não encontrado")
    return petiano_atualizado

@app.delete("/petianos/{id}")
def deletar_petiano(petiano_id: int, db: Session = Depends(get_db)):
    """Rota para deletar um petiano."""
    petiano_deletado = crud.deletar_petiano(db, petiano_id)
    if petiano_deletado is None:
        raise HTTPException(status_code=404, detail="Petiano não encontrado")
    return {"detail": "Petiano removido com sucesso"}

@app.delete("/tarefas")
def deletar_todos_petianos(db: Session = Depends(get_db)):
    """Rota para deletar todos os petianos."""
    crud.deletar_todos_petianos(db)
    return {"detail": "Todos os petianos foram removidos"}