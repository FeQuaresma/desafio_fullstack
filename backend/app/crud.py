from sqlalchemy.orm import Session
from . import models, schemas

# Função que puxa um tipo de ação pelo codigo da ação
def get_tipo_acao(db: Session, codigo_acao: int):
    return db.query(models.Tipo_acao).filter(models.Tipo_acao.codigo_acao == codigo_acao).first()

# Função que puxa um tipo de ação pelo nome da ação
def get_tipo_acao_by_nome(db: Session, nome_acao: str):
    return db.query(models.Tipo_acao).filter(models.Tipo_acao.nome_acao == nome_acao).first()

# Função que puxa todos os tipos de ação
def get_tipos_acao(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tipo_acao).offset(skip).limit(limit).all()

# Função que cria um novo tipo de ação, adiciona, sobe pro db e atualiza
def create_tipo_acao(db: Session, tipo_acao: schemas.TipoAcao):
    db_tipo_acao = models.Tipo_acao(**tipo_acao.model_dump())
    db.add(db_tipo_acao)
    db.commit()
    db.refresh(db_tipo_acao)
    return db_tipo_acao

# Função que puxa uma ação pelo id
def get_acao(db: Session, id: int):
    return db.query(models.Acao).filter(models.Acao.id == id).first()

# Função que puxa todas as ações
def get_acoes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Acao).offset(skip).limit(limit).all()

# Função que deleta uma ação
def delete_acao(db: Session, acao: schemas.Acao):
    db.delete(acao)
    db.commit()
    return {"ok":"deleted"}

# Função que atualiza uma função
def patch_acao(db: Session, id: int, acao_update: schemas.AcaoUpdate):
    db_acao = get_acao(db, id)
    if not db_acao:
        return None
    for key, value in acao_update.model_dump().items():
        if value is not None:
            setattr(db_acao, key, value)
    db.commit()
    db.refresh(db_acao)
    return db_acao

# Função que cria uma função
def create_acao(db: Session, acao: schemas.Acao):
    db_acao = models.Acao(**acao.model_dump())
    db.add(db_acao)
    db.commit()
    db.refresh(db_acao)
    return db_acao
