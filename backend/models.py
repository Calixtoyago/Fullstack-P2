from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

Prioridade = Literal["normal", "importante"]

class AvisosCreate(BaseModel):
    titulo: str = Field(min_length=3, max_length=40)
    mensagem: str = Field(min_length=3, max_length=400)
    autor: str = Field(min_length=3, max_length=40)
    prioridade: Prioridade

class AvisosResponse(AvisosCreate):
    publicado_em: datetime