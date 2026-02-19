

# Consultar o sql


from sqlalchemy.orm import Session
from app.db.models import Registro


class FileRepository:

    @staticmethod
    def salvar(db: Session, nome_arquivo: str, hash_arquivo: str):
        registro = Registro(
            nome=nome_arquivo,
            hash=hash_arquivo
        )
        db.add(registro)
        db.commit()
        db.refresh(registro)
        return registro
