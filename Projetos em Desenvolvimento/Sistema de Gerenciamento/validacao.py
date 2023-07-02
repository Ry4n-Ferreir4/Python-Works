"""
Codigos de Erro: 

1 = Usuario existente
2 = Label Vazia 
3 = Usuario Logado
4 = Usuario e/ou senha invalidos! 

"""

import sqlite3
import hashlib


def validacao(usuario, nome, cargo, senha):
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
