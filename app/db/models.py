

#estrutura das tabelas


from sqlalchemy import Column, Integer, String
from datetime import datetime
from app.db.database import Base

class Registro(Base):
    __tablename__ = "registros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    hash = Column(String, nullable=False)
    data = Column(String, default=lambda: datetime.now().isoformat())


