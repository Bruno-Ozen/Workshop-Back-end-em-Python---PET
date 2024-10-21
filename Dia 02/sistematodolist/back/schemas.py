from pydantic import BaseModel
from typing import List

class TarefaBase(BaseModel):
    """Esquema base para a tarefa."""
    descricao: str

class Tarefa(TarefaBase):
    """Esquema para exibição de uma tarefa."""
    id: int
    dono_id: int

    class Config:
        orm_mode = True  # Habilita compatibilidade com ORM

class UsuarioBase(BaseModel):
    """Esquema base para o usuário."""
    username: str

class UsuarioCriar(UsuarioBase):
    """Esquema para criação de um novo usuário."""
    username: str
    senha: str

class Usuario(UsuarioBase):
    """Esquema para exibição de um usuário."""
    id: int
    tarefas: List[Tarefa] = []

    class Config:
        orm_mode = True

class DadosToken(BaseModel):
    """Esquema para os dados contidos no token JWT."""
    username: str = None
