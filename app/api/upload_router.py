from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import shutil, os
from db.database import get_db
from services.hash_service import gerar_hash_arquivo
from services.integrity_service import IntegrityService
from core.utils import get_project_root

router = APIRouter(prefix="/uploads", tags=["Uploads"])

UPLOAD_DIR = os.path.join(get_project_root(), "uploads")

@router.post("/")
async def upload_arquivo(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    caminho = os.path.join(UPLOAD_DIR, file.filename)

    with open(caminho, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    hash_arquivo = gerar_hash_arquivo(caminho)

    registro = IntegrityService.registrar_arquivo(
        db,
        file.filename,
        hash_arquivo
    )

    return {
        "arquivo": registro.nome,
        "hash": registro.hash,
        "id": registro.id
    }

