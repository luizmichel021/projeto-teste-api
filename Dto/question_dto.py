from pydantic import BaseModel
from typing import List

class RespostaDTO(BaseModel):
    letra: str
    texto: str

class PerguntaDTO(BaseModel):
    id: int
    texto: str
    respostas: List[RespostaDTO]

class Config:
    orm_mode = True