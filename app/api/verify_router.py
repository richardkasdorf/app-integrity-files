from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.integrity_service import IntegrityService

router = APIRouter(prefix="/verify", tags=["Verificação"])

@router.get("/{nome_arquivo}")
def verificar_arquivo(nome_arquivo: str, db: Session = Depends(get_db)):
    resultado = IntegrityService.verificar_integridade(db, nome_arquivo)
    return resultado
