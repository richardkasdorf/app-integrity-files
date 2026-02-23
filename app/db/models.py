

#estrutura das tabelas


from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

#data = Column(DateTime, default=datetime.utcnow)

class Registro(Base):
    __tablename__ = "registros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    versao = Column(Integer, nullable=False)
    hash = Column(String, nullable=False)
    #data = Column(String, default=lambda: datetime.now().isoformat())
    data = Column(DateTime, default=datetime.utcnow)


