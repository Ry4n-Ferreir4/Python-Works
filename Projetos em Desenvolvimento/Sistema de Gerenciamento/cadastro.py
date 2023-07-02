import sqlite3
import hashlib


def cadastrar(usuario, nome, cargo, senha):
    banco = sqlite3.connect("DB.db")
    cursor = banco.cursor()
    senha_md5 = hashlib.md5(senha.encode()).hexdigest()
    cursor.execute(
        "INSERT INTO usuarios VALUES ('"
        + usuario
        + "', '"
        + nome
        + "', '"
        + cargo
        + "', '"
        + senha_md5
        + "')"
    )

    banco.commit()
    banco.close()
