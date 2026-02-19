import hashlib

#Gerar HASH para o arquivo
def gerar_hash_arquivo(caminho_arquivo):
    sha256 = hashlib.sha256()

    with open(caminho_arquivo, "rb") as f:
        for bloco in iter(lambda: f.read(4096), b""):
            sha256.update(bloco)

    return sha256.hexdigest()
