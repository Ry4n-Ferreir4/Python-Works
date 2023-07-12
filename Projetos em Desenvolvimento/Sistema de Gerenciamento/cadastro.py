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

        banco_vendas = sqlite3.connect("Vendas.db")
        cursor_vendas = banco_vendas.cursor()
        cursor_vendas.execute(
            f"CREATE TABLE IF NOT EXISTS {nome} (IDVenda INTEGER PRIMARY KEY, Produto TEXT, Valor REAL,Quantidade INTEGER, Vendedor TEXT,Data TEXT)"
        )

        banco_vendas.commit()
        banco.commit()
    except sqlite3.Error as erro:
        print(erro)
    finally:
        banco_vendas.close()
        banco.close()


def cadastrar_produto(cod_prod, nome_produto, quantidade, preco):
    banco = sqlite3.connect("Estoque.db")
    cursor = banco.cursor()

    cursor.execute(f"SELECT CodProd FROM produtos WHERE CodProd = '{cod_prod}'")
    produto = cursor.fetchall()
    print(produto[0][0])

    if produto[0][0] != "":
        cursor.execute(
            f"UPDATE produtos SET qtdprod = qtdprod + {quantidade} WHERE Codprod = {cod_prod}"
        )
        print("Produto Atualizado! ")
        banco.commit()
        banco.close()
    else:
        try:
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
            banco.commit()
            banco.close()
