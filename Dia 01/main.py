from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel, EmailStr, field_validator

# Exemplo do slide

app = FastAPI() # criação da aplicação 

@app.get("/")
async def root():
    return {"message": "Hello World"}


# EXERCICIO 1 - validação de e-mail

class EmailRequest(BaseModel): # BaseModel é uma classe do Pydantic que serve como base para a criação de modelos
    email: EmailStr

@app.post("/email") # rota para validar e-mail

async def valida_email(request: EmailRequest): 
    try:
        return  {"message": "E-mail válido", "email": request.email}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# EXERCICIO 2 - validação de celular

class Celular(BaseModel):
    celular: str

    @field_validator('celular')
    def validacao(cls, celular: str) -> str:
        if len(celular) != 11 or not celular.isdigit(): # isdigit() verifica se a string contém apenas números
            raise ValueError('Número de celular inválido')
        return celular

@app.get('/celular')
async def valida_celular(celularRequest: str):
    try:
        celular = Celular(celular=celularRequest)
        return {"message": 'Número de celular válido', "celular": celular.celular}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# EXERCÍCIO 3 - validação de CPF

class CPF(BaseModel):
    cpf: str

    @field_validator('cpf')
    def validar_cpf(cls, cpf: str) -> str:

        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError('CPF inválido: deve ter 11 dígitos e conter apenas números.')

        if cpf == cpf[0] * len(cpf):
            raise ValueError('CPF inválido: não pode ser uma sequência de dígitos iguais.')
        return cpf

@app.get("/cpf")
async def valida_cpf(cpfRequest: str):
    '''
    essa funcao valida cpf
    '''
    try:
        cpf = CPF(cpf=cpfRequest)
        return {"message": "CPF válido", "cpf": cpf}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))