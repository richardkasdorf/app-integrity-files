# from sqlalchemy.orm import Session
# from app.repositories.file_repository import FileRepository


# class IntegrityService:

#     @staticmethod
#     def registrar_arquivo(db: Session, nome: str, hash_arquivo: str):
#         return FileRepository.salvar(db, nome, hash_arquivo)


from fastapi import APIRouter
from app.services.hash_service import gerar_hash_arquivo
import sqlite3

router = APIRouter()

def verificar_integridade(nome_arquivo, caminho):
    conn = sqlite3.connect("registros.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT hash FROM registros WHERE nome=? ORDER BY id DESC LIMIT 1",
        (nome_arquivo,)
    )

    resultado = cursor.fetchone()
    conn.close()

    if not resultado:
        return "Arquivo não registrado"

    hash_registrado = resultado[0]
    hash_atual = gerar_hash_arquivo(caminho)

    if hash_registrado == hash_atual:
        return "Arquivo íntegro ✅"
    else:
        return "ALERTA: arquivo adulterado ⚠️"


print(verificar_integridade(
    "testando integridade 17022026.txt",
    "testando integridade 17022026.txt"
))
