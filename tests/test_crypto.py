from app.services.hash_service import gerar_hash_arquivo

def test_hash_consistente(tmp_path):
    arquivo = tmp_path / "teste.txt"
    arquivo.write_text("dados")

    hash1 = gerar_hash_arquivo(arquivo)
    hash2 = gerar_hash_arquivo(arquivo)

    assert hash1 == hash2




    