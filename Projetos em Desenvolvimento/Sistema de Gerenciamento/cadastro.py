import sqlite3
import hashlib


def cadastrar_usuario(usuario, nome, cargo, senha):
    try:
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
    except sqlite3.Error as erro:
        print(erro)
    finally:
        banco.close()


def cadastrar_produto(cod_prod, nome_produto, quantidade, preco):
    try:
        banco = sqlite3.connect("Estoque.db")
        cursor = banco.cursor()

        cursor.execute(
            "INSERT INTO produtos VALUES ('"
            + cod_prod
            + "','"
            + nome_produto
            + "', '"
            + quantidade
            + "', '"
            + preco
            + "')"
        )

        banco.commit()
    except sqlite3.Error as erro:
        print(erro)
    finally:
        banco.close()
