from pydantic import BaseModel
from typing import Dict

class RespostasUsuarioDTO(BaseModel):
    respostas: Dict[int, str]

class Config:
    orm_mode = True