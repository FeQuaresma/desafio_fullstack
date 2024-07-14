from pydantic import BaseModel
from datetime import date

class TipoAcaoBase(BaseModel):
    nome_acao: str

class TipoAcaoCreate(TipoAcaoBase):
    pass

class TipoAcao(TipoAcaoBase):
    codigo_acao: int

    class Config:
        orm_mode = True


class AcaoBase(BaseModel):
    investimento: float
    data_prevista: date | None = None
    data_cadastro: date | None = None

class AcaoCreate(AcaoBase):
    codigo_acao: int

class Acao(AcaoBase):
    id: int
    codigo_acao: int
    tipo_acao: TipoAcao

    class Config:
        orm_mode = True
