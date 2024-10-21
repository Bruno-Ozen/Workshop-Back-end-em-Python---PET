from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel, EmailStr, field_validator

app = FastAPI()

@app.get("/")

async def root():
    return {"Hello": "World"}

# EXERCÍCIO 1
# Criar validação de email com fast api

class EmailRequest(BaseModel):
    email: EmailStr

@app.post("/email")
async def valida_email(request: EmailRequest):
    try:
        return {"message": "Email válido", "email": request.email}
    except:
        raise HTTPException(status_code=400, detail=str(e))

# EXERCÍCIO 2
# Criar validação de celular com fast api

class PhoneRequest(BaseModel):
    telefone: str

    @field_validator("telefone")
    def valida_telefone(cls, valor) -> str:
        if len(valor) == 11 and valor.isdigit():
            return valor
        else:
            raise ValueError("O número deve conter 11 dígitos, sendo os 2 primeiros para o DDD.")
            
@app.post("/phone")
async def valida_telefone(request: PhoneRequest):
    try:
        celular = PhoneRequest(telefone=PhoneRequest)
        return {"message": "Número de celular válido", "celular": celular.telefone}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# EXERCÍCIO 3
# Validação de cpf usando fastAPI e pydantic
class cpfRequest(BaseModel):
    cpf: str

    @field_validator
    def valida_cpf(cls, valor) -> str:
        if len(valor) != 11 and not valor.isdigit():
            raise ValueError("O cpf deve conter 11 dígitos, e ser um número.")
        if valor == valor[0] * len(valor):
            raise ValueError("O cpf não deve conter todos os dígitos iguais. ")
        return valor
    
@app.post("/cpf")
async def valida_cpf(request: cpfRequest):
    try:
        cpf = cpfRequest(cpf = cpfRequest)
        return {"message": "CPF validado com sucesso", "cpf": cpf.cpf}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# EXERCÍCIO 4
# Juntar todos os exercícios anteriores em um

class Pessoa(BaseModel):
    nome: str
    email: EmailStr
    cpf: str
    telefone: str

    @field_validator("telefone")
    def valida_telefone(cls, valor) -> str:
        if len(valor) == 11 and valor.isdigit():
            return valor
        else:
            raise ValueError("O número deve conter 11 dígitos, sendo os 2 primeiros para o DDD.")
        
    @field_validator
    def valida_cpf(cls, valor) -> str:
        if len(valor) != 11 and not valor.isdigit():
            raise ValueError("O cpf deve conter 11 dígitos, e ser um número.")
        if valor == valor[0] * len(valor):
            raise ValueError("O cpf não deve conter todos os dígitos iguais. ")
        return valor        

@app.post("/pessoa/")
async def valida_pessoa(request: Pessoa):
    try:
        nome = Pessoa(nome=Pessoa)
        return {"message": "Pessoa validada com sucesso",
                "nome": nome.nome
                }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))