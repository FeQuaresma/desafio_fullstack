from sqlalchemy.orm import Session
from . import models, schemas


def get_tipo_acao(db: Session, codigo_acao: int):
    return db.query(models.Tipo_acao).filter(models.Tipo_acao.codigo_acao == codigo_acao).first()


def get_tipo_acao_by_nome(db: Session, nome_acao: str):
    return db.query(models.Tipo_acao).filter(models.Tipo_acao.nome_acao == nome_acao).first()


def get_tipos_acao(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tipo_acao).offset(skip).limit(limit).all()


def create_tipo_acao(db: Session, tipo_acao: schemas.TipoAcao):
    db_tipo_acao = models.Tipo_acao(**tipo_acao.model_dump())
    db.add(db_tipo_acao)
    db.commit()
    db.refresh(db_tipo_acao)
    return db_tipo_acao


def get_acao(db: Session, id: int):
    return db.query(models.Acao).filter(models.Acao.id == id).first()

def get_acoes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Acao).offset(skip).limit(limit).all()

def create_acao(db: Session, acao: schemas.Acao, codigo_acao: int):
    # db_acao = models.Acao(**acao.model_dump(), codigo_acao=codigo_acao)
    db_acao = models.Acao(**acao.model_dump())
    db.add(db_acao)
    db.commit()
    db.refresh(db_acao)
    return db_acao
