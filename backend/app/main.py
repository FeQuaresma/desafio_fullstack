from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import crud, models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tipos_acao/", response_model=list[schemas.TipoAcao])
def read_tipos_acao(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tipos_acao = crud.get_tipos_acao(db, skip=skip, limit=limit)
    return tipos_acao

@app.get("/tipo_acao/{codigo_acao}", response_model=schemas.TipoAcao)
def read_tipo_acao(codigo_acao: int, db: Session = Depends(get_db)):
    db_tipo_acao = crud.get_tipo_acao(db, codigo_acao=codigo_acao)
    if db_tipo_acao is None:
        raise HTTPException(status_code=404, detail="Tipo de ação não encontrado")
    return db_tipo_acao

@app.post("/tipo_acao/", response_model=schemas.TipoAcao)
def create_tipo_acao(tipo_acao: schemas.TipoAcaoCreate, db: Session = Depends(get_db)):
    db_tipo_acao = crud.get_tipo_acao_by_nome(db, nome_acao=tipo_acao.nome_acao)
    if db_tipo_acao:
        raise HTTPException(status_code=400, detail="Tipo de ação já registrado")
    return crud.create_tipo_acao(db=db, tipo_acao=tipo_acao)

@app.post("/acao/", response_model=schemas.Acao)
def create_acao(acao: schemas.AcaoCreate, db: Session = Depends(get_db)):
    return crud.create_acao(db=db, acao=acao)

@app.get("/acao/{id}", response_model=schemas.Acao)
def read_acao(id: int, db: Session = Depends(get_db)):
    return crud.get_acao(db, id=id)

@app.delete("/acao/{id}")
def delete_acao(id: int, db: Session = Depends(get_db)):
    db_acao = crud.get_acao(db, id=id)
    return crud.delete_acao(db, db_acao)

@app.get("/acoes/", response_model=list[schemas.Acao])
def read_acoes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    acoes = crud.get_acoes(db, skip=skip, limit=limit)
    return acoes

@app.patch("/acao/{id}", response_model=schemas.Acao)
def patch_acao(id: int, acao_update: schemas.AcaoUpdate, db: Session = Depends(get_db)):
    db_acao = crud.patch_acao(db, id=id, acao_update=acao_update)
    if db_acao is None:
        raise HTTPException(status_code=404, detail="Ação não encontrada")
    return db_acao
