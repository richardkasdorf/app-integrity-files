from sqlalchemy.orm import Session
from db.models import Registro

class FileRepository:

    @staticmethod
    def criar_registro(db: Session, nome: str, hash: str):
        ultimo = FileRepository.buscar_ultimo_por_nome(db, nome)
        nova_versao = 1 if not ultimo else ultimo.versao + 1
        registro = Registro(
            nome=nome,
            hash=hash,
            versao=nova_versao
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