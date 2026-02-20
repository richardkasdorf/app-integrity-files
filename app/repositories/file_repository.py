

# Consultar o sql / banco de dados


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


    @staticmethod
    def buscar_ultimo_por_nome(db: Session, nome: str):
        return (
            db.query(Registro)
            .filter(Registro.nome == nome)
            .order_by(Registro.id.desc())
            .first()
        )