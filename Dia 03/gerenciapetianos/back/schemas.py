from pydantic import BaseModel
from typing import List

class PetianoBase(BaseModel):
    """Esquema base para a tarefa."""
    nome: str
    cpf: str
    email: str
    curso: str

class Petiano(PetianoBase):
    "Esquema para exibição de um petiano."
    id: int

    class Config:
        orm_mode = True
