from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import shutil, os
from app.db.database import get_db
from app.services.hash_service import gerar_hash_arquivo
from app.services.integrity_service import IntegrityService

router = APIRouter(prefix="/uploads", tags=["Uploads"])

UPLOAD_DIR = "uploads"

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

# from fastapi import APIRouter, UploadFile, Depends, File
# import shutil
# from app.services.hash_service import gerar_hash_arquivo
# from app.database import salvar_registro

# router = APIRouter(prefix="/uploads", tags=["uploads"])

# @router.post("/upload/")
# async def upload_arquivo(file: UploadFile = File(...)):
#     caminho = f"uploads/{file.filename}"

#     with open(caminho, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     hash_arquivo = gerar_hash_arquivo(caminho)
#     salvar_registro(file.filename, hash_arquivo)

#     return {"arquivo": file.filename, "hash": hash_arquivo}