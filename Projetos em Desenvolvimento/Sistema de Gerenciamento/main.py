import typing
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from ui_main import Ui_TelaMain
from ui_telaCadastro import Ui_Cadastro
from ui_telaLogin import Ui_Login

from validacao import validacao, validacao_login
from cadastro import cadastrar
import sqlite3
import pandas as pd


class Tela_principal(QMainWindow, Ui_TelaMain):
    def __init__(self) -> None:
        super(Tela_principal, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela de Produtos")

        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_produtos.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_table)
        )
        self.btn_logout.clicked.connect(logout)
        self.btn_venda.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_venda)
        )
        self.btn_atualizar.clicked.connect(lambda: self.listar_produtos())
        self.listar_produtos()

    def listar_produtos(self):
        # Conecte ao banco de dados
        conn = sqlite3.connect("Estoque.db")
        cursor = conn.cursor()

        # Recupere os produtos do banco de dados
        cursor.execute("SELECT * FROM Produtos")
        produtos = cursor.fetchall()

        # Defina o número de linhas e colunas da tabela
        self.tw_estoque.setRowCount(len(produtos))
        self.tw_estoque.setColumnCount(3)

        # Preencha a tabela com os produtos
        for row, produto in enumerate(produtos):
            for col, value in enumerate(produto):
                item = QTableWidgetItem(str(value))
                self.tw_estoque.setItem(row, col, item)

        # Feche a conexão com o banco de dados
        conn.close()


class Tela_login(QMainWindow, Ui_Login):
    def __init__(self) -> None:
        super(Tela_login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login")

    def login_ui(self):
        usuario = str(tela_login.lineEdit.text()).upper()
        senha = tela_login.lineEdit_2.text()

        try:
            if validacao_login(usuario, senha) == 3:
                tela_principal.show()
                tela_login.close()
                tela_login.lineEdit.setText("")
                tela_login.lineEdit_2.setText("")

            elif validacao_login(usuario, senha) == 4:
                tela_login.label_4.setStyleSheet("color: rgb(255, 0, 0);")
                tela_login.label_4.setText("Usuario e/ou senha inválidos")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados aqui: ", erro)


class Tela_cadastro(QMainWindow, Ui_Cadastro):
    def __init__(self) -> None:
        super(Tela_cadastro, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cadastro")

    def cadastrar_ui(self):
        usuario = str(tela_cadastro.lineEdit.text()).upper()
        nome = str(tela_cadastro.lineEdit_4.text()).capitalize()
        cargo = tela_cadastro.lineEdit_3.text()
        senha = tela_cadastro.lineEdit_2.text()

        if validacao(usuario, nome, cargo, senha) == 0:
            try:
                cadastrar(usuario, nome, cargo, senha)
                tela_cadastro.label_4.setText("")
                tela_login.label_4.setStyleSheet("color: rgb(85, 255, 0);")
                tela_login.label_4.setText("Usuario Cadastrado com Sucesso")
                tela_cadastro.lineEdit.setText("")
                tela_cadastro.lineEdit_4.setText("")
                tela_cadastro.lineEdit_3.setText("")
                tela_cadastro.lineEdit_2.setText("")

                tela_login.show()
                tela_cadastro.close()

            except sqlite3.Error as erro:
                print("Erro ao inserir os dados aqui: ", erro)

        elif validacao(usuario, nome, cargo, senha) == 1:
            tela_cadastro.label_4.setText("Usuario Já Existente")

        elif validacao(usuario, nome, cargo, senha) == 2:
            tela_cadastro.label_4.setText("Preencha todos os campos")


def iniciar_tela_cadastro():
    tela_login.close()
    tela_cadastro.show()


def logout():
    tela_login.show()
    tela_principal.close()


app = QApplication(sys.argv)
tela_principal = Tela_principal()
tela_login = Tela_login()
tela_cadastro = Tela_cadastro()

tela_login.pushButton_2.clicked.connect(iniciar_tela_cadastro)
tela_cadastro.pushButton.clicked.connect(Tela_cadastro.cadastrar_ui)
tela_login.pushButton.clicked.connect(Tela_login.login_ui)


if __name__ == "__main__":
    tela_login.show()
    app.exec_()
