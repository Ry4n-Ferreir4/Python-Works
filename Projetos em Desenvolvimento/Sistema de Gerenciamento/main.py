from PyQt5 import uic, QtWidgets
from validacao import validacao, validacao_login
from cadastro import cadastrar
import sqlite3


def iniciar_tela_cadastro():
    tela_login.close()
    tela_cadastro.show()


def iniciar_tela_login():
    tela_login.show()
    tela_principal.close()


def login_ui():
    usuario = str(tela_login.lineEdit.text()).upper()
    senha = tela_login.lineEdit_2.text()

    try:
        if validacao_login(usuario, senha) == 3:
            tela_principal.show()
            tela_login.lineEdit.setText("")
            tela_login.lineEdit_2.setText("")

        elif validacao_login(usuario, senha) == 4:
            tela_login.label_4.setStyleSheet("color: rgb(255, 0, 0);")
            tela_login.label_4.setText("Usuario e/ou senha inválidos")

    except sqlite3.Error as erro:
        print("Erro ao inserir os dados aqui: ", erro)


def cadastrar_ui():
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


app = QtWidgets.QApplication([])
tela_login = uic.loadUi("Tela_login.ui")
tela_cadastro = uic.loadUi("Tela_cadastro.ui")
tela_principal = uic.loadUi("Produtos_main.ui")

tela_principal.pushButton.clicked.connect(iniciar_tela_login)
tela_login.pushButton_2.clicked.connect(iniciar_tela_cadastro)
tela_cadastro.pushButton.clicked.connect(cadastrar_ui)
tela_login.pushButton.clicked.connect(login_ui)

tela_login.show()
app.exec()
