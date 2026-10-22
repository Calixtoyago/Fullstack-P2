from datetime import datetime
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from models import AvisosCreate, AvisosResponse
import uvicorn

app = FastAPI(
    title="API de Avisos Acadêmicos",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8080",
        "http://127.0.0.1:8080",
    ],
    allow_methods=["*"],
    allow_headers=["*"]
)

avisos: list[AvisosResponse] = []

@app.get("/api/avisos", response_model=list[AvisosResponse])
def listar_avisos():
    return avisos

@app.post("/api/avisos", response_model=AvisosResponse, status_code=status.HTTP_201_CREATED)
def criar_aviso(dados: AvisosCreate):
    aviso = AvisosResponse(
        id=len(avisos) + 1,
        publicado_em=datetime.now(),
        **dados.model_dump(),
    )

    avisos.append(aviso)
    return aviso

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)