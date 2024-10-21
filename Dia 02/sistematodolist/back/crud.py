from sqlalchemy.orm import Session
from models import Usuario, Tarefa
from schemas import UsuarioCriar, TarefaBase

def criar_tarefa(db, tarefa, usuario_id):

    tarefa_db = Tarefa(descricao=tarefa.descricao, dono_id=usuario_id)
    db.add(tarefa_db)
    db.commit()
    db.refresh(tarefa_db)
    return tarefa_db

def obter_tarefas(db, usuario_id):
    return db.query(Tarefa).filter(Tarefa.dono_id == usuario_id).all()

def deletar_tarefa(db, tarefa_id, usuario_id):
    tarefa_db = db.query(Tarefa).filter(Tarefa.id == tarefa_id, Tarefa.dono_id == usuario_id).first()
    if tarefa_db:
        db.delete(tarefa_db)
        db.commit()
    return tarefa_db

def atualizar_tarefa(db, tarefa_id, usuario_id, descricao):
    tarefa_db = db.query(Tarefa).filter(Tarefa.id == tarefa_id, Tarefa.dono_id == usuario_id).first()
    if tarefa_db:
        tarefa_db.descricao = descricao
        db.commit()
        db.refresh(tarefa_db)
    return tarefa_db

def deletar_todas_tarefas(db, usuario_id):
    db.query(Tarefa).filter(Tarefa.dono_id == usuario_id).delete()
    db.commit()