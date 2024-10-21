from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexão com o banco de dados SQLite
URL_BANCO_DE_DADOS = "sqlite:///./app.db"

engine = create_engine(
    URL_BANCO_DE_DADOS, connect_args={"check_same_thread": False}
)

# Cria uma sessão local do banco de dados
SessaoLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para as tabelas do SQLAlchemy
Base = declarative_base()
