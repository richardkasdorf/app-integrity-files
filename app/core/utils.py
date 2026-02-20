import os


#Interage com pasta /uploads na raiz

def get_project_root():
    return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

def get_upload_path(nome_arquivo: str):
    return os.path.join(get_project_root(), "uploads", nome_arquivo)
