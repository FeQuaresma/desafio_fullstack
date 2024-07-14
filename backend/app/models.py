from sqlalchemy import Column, ForeignKey, Integer, String, Date, Double
from sqlalchemy.orm import relationship

from .database import Base

class Tipo_acao(Base):
  __tablename__ = "tipo_acao"
  
  codigo_acao = Column(Integer, primary_key=True, index=True, autoincrement=True)
  nome_acao = Column(String(100), nullable=False)

  acoes = relationship("Acao", back_populates="tipo_acao")

class Acao(Base):
  __tablename__ = "acao"

  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  codigo_acao = Column(Integer, ForeignKey("tipo_acao.codigo_acao"))
  investimento = Column(Double)
  data_prevista = Column(Date)
  data_cadastro = Column(Date)

  tipo_acao = relationship("Tipo_acao", back_populates="acoes")