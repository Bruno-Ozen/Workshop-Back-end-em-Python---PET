from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from models import Base
from database import engine, SessaoLocal
import schemas, crud

ID_USUARIO = 1

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def get_db():
    db = SessaoLocal()

    try:
        yield db
    finally:
        db.close()

@app.post("/tarefas", response_model=schemas.Tarefa)
def criar_nova_tarefa(tarefa: schemas.TarefaBase, db: Session = Depends(get_db)):
    return crud.criar_tarefa(db, tarefa, usuario_id=ID_USUARIO)

@app.get("/tarefas", response_model=List[schemas.Tarefa])
def ler_tarefas(db: Session = Depends(get_db)):
    return crud.obter_tarefas(db, usuario_id=ID_USUARIO)

@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id, db: Session = Depends(get_db)):

    tarefa_deletada = crud.deletar_tarefa(db, tarefa_id, usuario_id=ID_USUARIO)
    if tarefa_deletada is None:
        raise HTTPException(status_code=404, detail="Tarefa não foi encontrada")
    return {"detail": "Tarefa removida com sucesso."}

@app.delete("/tarefas")
def deletar_todas_tarefas(db: Session = Depends(get_db)):
    crud.deletar_todas_tarefas(db, usuario_id=ID_USUARIO)
    return {"detail": "Todas as tarefas foram removidas"}

@app.put("/tarefas/{tarefa_id}", response_model=schemas.Tarefa)
def atualizar_tarefa(tarefa_id, tarefa:schemas.TarefaBase, db: Session = Depends(get_db)):
    tarefa_atualizada = crud.atualizar_tarefa(db, tarefa_id, usuario_id=ID_USUARIO, descricao=tarefa.descricao)

    if tarefa_atualizada is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa_atualizada