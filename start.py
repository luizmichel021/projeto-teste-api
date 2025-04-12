from fastapi import FastAPI
from Connection import Base, engine
from Models import question, answer, answer_key  # importa os models pra registrar no Base

app = FastAPI(
    title="Questionário API",
    description="Protótipo de API para sorteio de perguntas e validação de respostas",
    version="1.0.0"
)

# Cria as tabelas no banco, se ainda não existirem
Base.metadata.create_all(bind=engine)

# Rota de teste
@app.get("/")
def root():
    return {"message": "API está funcionando!"}