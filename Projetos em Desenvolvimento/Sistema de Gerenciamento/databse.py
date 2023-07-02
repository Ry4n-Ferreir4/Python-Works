import sqlite3


class Database:
    def __init__(self, nome="DB.db") -> None:
        self.nome = nome

    def conecta(self):
        self.conexao = sqlite3.connect(self.nome)

    def close_conexao(self):
        try:
            self.conexao.close()
        except sqlite3.Error as erro:
            print("Erro ao inserir os dados aqui: ", erro)


if __name__ == "__main__":
    db = Database()
    db.conecta()
    db.close_conexao()
