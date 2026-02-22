import sqlite3

conn = sqlite3.connect("registros.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM registros")

linhas = cursor.fetchall()

for linha in linhas:
    print(linha)

conn.close()