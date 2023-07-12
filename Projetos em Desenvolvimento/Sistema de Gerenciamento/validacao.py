"""
Codigos de Erro: 

1 = existente
2 = Label Vazia 
3 = Usuario Logado / Produto Válido
4 = Usuario e/ou senha invalidos! 
5 = Produto inválido
6 = Produto atualizado! 

"""

import sqlite3
import hashlib


def validacao_cadastro(usuario, nome, cargo, senha):
    banco = sqlite3.connect("DB.db")
    cursor = banco.cursor()
    cursor.execute(f"SELECT usuario FROM usuarios WHERE usuario = '{usuario}'")
    usuario_db = cursor.fetchall()

    if usuario == "" or nome == "" or cargo == "" or senha == "":
        return 2
    else:
        if len(usuario_db) > 0 and usuario == usuario_db[0][0]:
            return 1
        else:
            return 0


def validacao_login(usuario, senha):
    banco = sqlite3.connect("DB.db")
    cursor = banco.cursor()
    cursor.execute(f"SELECT senha FROM usuarios WHERE usuario = '{usuario}'")
    senhauser_md5 = hashlib.md5(senha.encode()).hexdigest()
    senha_db = cursor.fetchall()

    if len(senha_db) > 0 and senhauser_md5 == senha_db[0][0]:
        return 3
    else:
        return 4


def validacao_cadastro_produtos(cod_prod, produto, quantidade, preco):
    str(produto).strip("' ")
    str(quantidade).strip("' ")
    str(cod_prod).strip("' ")
    str(cod_prod).replace(" ", "")
    banco = sqlite3.connect("Estoque.db")
    cursor = banco.cursor()
    cursor.execute(f"SELECT Nome FROM Produtos WHERE Nome = '{produto}';")
    produto_db = cursor.fetchall()

    cursor.execute(f"SELECT CodProd FROM produtos WHERE CodProd = '{cod_prod}'")
    produto_existente = cursor.fetchall()
    try:
        if produto_existente[0][0] != "":
            return 3
        else:
            if produto == "" or quantidade == "" or preco == "" or cod_prod == "":
                return 2
            elif (
                produto.isdigit()
                or quantidade == "0"
                or preco == 0
                or not cod_prod.isdigit()
            ):
                print("Digite um produto válido")
                return 5
            elif len(produto_db) > 0:
                return 1
            else:
                return 3
    except:
        return 5
