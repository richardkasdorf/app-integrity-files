# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from app.core.config import DATABASE_URL

# engine = create_engine(
#     DATABASE_URL,
#     connect_args={"check_same_thread": False}  # necessário para SQLite
# )

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )

# Base = declarative_base()


# # Dependency para FastAPI
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



# import sqlite3
# from datetime import datetime

# #conexão com o banco
# def salvar_registro(nome_arquivo, hash_arquivo):
#     conn = sqlite3.connect("registros.db")
#     cursor = conn.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS registros (
#             id INTEGER PRIMARY KEY,
#             nome TEXT,
#             hash TEXT,
#             data TEXT
#         )
#     """)

#     cursor.execute(
#         "INSERT INTO registros (nome, hash, data) VALUES (?, ?, ?)",
#         (nome_arquivo, hash_arquivo, datetime.now().isoformat())
#     )

#     conn.commit()
#     conn.close()
