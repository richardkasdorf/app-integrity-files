from sqlalchemy.orm import Session
from app.services.hash_service import gerar_hash_arquivo
from app.repositories.file_repository import FileRepository
from app.core.utils import get_upload_path
import os

class IntegrityService:

    @staticmethod
    def verificar_integridade(db: Session, nome_arquivo: str):
        registro = FileRepository.buscar_ultimo_por_nome(db, nome_arquivo)

        if not registro:
            return {
                "status": "nao_registrado",
                "mensagem": "Arquivo não registrado"
            }

        caminho = get_upload_path(nome_arquivo)

        if not os.path.exists(caminho):
            return {
                "status": "nao_encontrado",
                "mensagem": "Arquivo não encontrado na pasta uploads"
            }

        hash_atual = gerar_hash_arquivo(caminho)

        if registro.hash == hash_atual:
            return {
                "status": "integro",
                "mensagem": "Arquivo íntegro ✅"
            }
        else:
            return {
                "status": "adulterado",
                "mensagem": "ALERTA: arquivo adulterado ⚠️"
            }

