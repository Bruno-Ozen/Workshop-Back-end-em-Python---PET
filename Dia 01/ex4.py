from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel, EmailStr, field_validator

app = FastAPI()

class Pessoa(BaseModel):
    nome: str 
    email: EmailStr  # EmailStr é um tipo de dado do Pydantic que já faz a validação de e-mail automaticamente
    cpf: str 
    telefone: str 

    # Função para validar o nome
    @field_validator('nome')
    def validar_nome(cls, nome: str) -> str:
        if not nome.isalpha(): # isalpha() verifica se a string contém apenas letras
            raise ValueError('Nome inválido')
        return nome

    # Função para validar o celular
    @field_validator('telefone')
    def validar_celular(cls, telefone: str) -> str:
        
        if len(telefone) != 11 or not telefone.isdigit(): # isdigit() verifica se a string contém apenas números
            raise ValueError('Número de celular inválido: deve ter 11 dígitos e conter apenas números.')

        return telefone

    # Função para validar o CPF
    @field_validator('cpf')
    def validar_cpf(cls, cpf: str) -> str:  

        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError('CPF inválido: deve ter 11 dígitos e conter apenas números.')

        if cpf == cpf[0] * len(cpf): # verifica se o primeiro dígito é igual a todos os outros dígitos 
            raise ValueError('CPF inválido: não pode ser uma sequência de dígitos iguais.')
       
        return cpf
        
@app.post("/pessoa/") # por fim, precisa de um POST para criar a pessoa 
async def criar_pessoa(pessoa: Pessoa):
    try:
        return {
            "mensagem": "Pessoa criada com sucesso!",
            "dados": pessoa
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))