import typing
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from ui_main import Ui_TelaMain
from ui_telaCadastro import Ui_Cadastro
from ui_telaLogin import Ui_Login
from ui_saida import Ui_tela_saida

from validacao import validacao_cadastro, validacao_login, validacao_cadastro_produtos
from cadastro import cadastrar_usuario, cadastrar_produto
from saidas import venda_produto
import sqlite3


class Tela_principal(QMainWindow, Ui_TelaMain):
    def __init__(self, tela_saida) -> None:
        super(Tela_principal, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela de Produtos")

        self.tela_saida = tela_saida
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_produtos.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_table)
        )
        self.btn_logout.clicked.connect(logout)
        self.btn_venda.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_venda)
        )
        self.btn_atualizar.clicked.connect(lambda: self.atualizar())
        self.listar_produtos()
        self.btn_cadastrar.clicked.connect(lambda: self.cadastrar_produtos())
        self.btn_open.clicked.connect(lambda: self.procurar_produtos())
        self.btn_gerar.clicked.connect(lambda: self.abrir_saida())

    def atualizar(self):
        self.listar_produtos()
        self.tela_saida.listar_venda()

    def abrir_saida(self):
        tela_saida.show()

    def listar_produtos(self):
        conn = sqlite3.connect("Estoque.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()

        # Define o número de linhas e colunas da tabela
        self.tw_estoque.setRowCount(len(produtos))
        self.tw_estoque.setColumnCount(4)

        # Preencher a tabela com os produtos
        for row, produto in enumerate(produtos):
            for col, value in enumerate(produto):
                item = QTableWidgetItem(str(value))
                self.tw_estoque.setItem(row, col, item)
        conn.close()

    def cadastrar_produtos(self):
        cod_prod = self.lineEdit_4.text()
        produto = self.lineEdit.text()
        quantidade = self.lineEdit_2.text()
        preco = str(f"{self.lineEdit_3.text()}")
        preco_formatado = preco.lstrip("0")
        msg_cadastrar_produto = ""

        if (
            validacao_cadastro_produtos(cod_prod, produto, quantidade, preco_formatado)
            == 2
        ):
            self.msg_box.setStyleSheet("color: rgb(255, 0, 0);")
            msg_cadastrar_produto = "Produto Invalido!"
        elif (
            validacao_cadastro_produtos(cod_prod, produto, quantidade, preco_formatado)
            == 1
        ):
            self.msg_box.setStyleSheet("color: rgb(255, 0, 0);")
            msg_cadastrar_produto = "Produto já cadastrado!"
        elif (
            validacao_cadastro_produtos(cod_prod, produto, quantidade, preco_formatado)
            == 5
        ):
            self.msg_box.setStyleSheet("color: rgb(255, 0, 0);")
            msg_cadastrar_produto = "Produto Inválido!"
        elif (
            validacao_cadastro_produtos(cod_prod, produto, quantidade, preco_formatado)
            == 6
        ):
            self.msg_box.setStyleSheet("color: rgb(85, 255, 0);")
            msg_cadastrar_produto = "Produto Atualizado!"

        else:
            try:
                cadastrar_produto(cod_prod, produto, quantidade, preco_formatado)
                self.msg_box.setStyleSheet("color: rgb(85, 255, 0)")
                msg_cadastrar_produto = "Produto cadastrado com sucesso!"
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.lineEdit_4.setText("")

            except:
                self.msg_box.setStyleSheet("color: red;")
                msg_cadastrar_produto = "Erro ao cadastrar produtos"
        self.msg_box.setText(f"{msg_cadastrar_produto}")

    def procurar_produtos(self):
        cod_prod = self.txt_file.text()
        try:
            conn = sqlite3.connect("Estoque.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM Produtos WHERE Codprod = '{cod_prod}'")
            produtos = cursor.fetchall()

            self.tw_estoque.setRowCount(len(produtos))
            self.tw_estoque.setColumnCount(4)

            for row, produto in enumerate(produtos):
                for col, value in enumerate(produto):
                    item = QTableWidgetItem(str(value))
                    self.tw_estoque.setItem(row, col, item)
            conn.close()
            cod_prod = self.txt_file.setText("")
        except:
            pass


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
                tela_saida.set_vendedor(usuario)

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

        if validacao_cadastro(usuario, nome, cargo, senha) == 0:
            try:
                cadastrar_usuario(usuario, nome, cargo, senha)
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

        elif validacao_cadastro(usuario, nome, cargo, senha) == 1:
            tela_cadastro.label_4.setText("Usuario Já Existente")

        elif validacao_cadastro(usuario, nome, cargo, senha) == 2:
            tela_cadastro.label_4.setText("Preencha todos os campos")


class Tela_saida(QMainWindow, Ui_tela_saida):
    def __init__(self) -> None:
        super(Tela_saida, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Saida")
        self.btn_gerar_saida.clicked.connect(lambda: self.venda())

    def set_vendedor(self, vendedor):
        self.vendedor = str(vendedor).capitalize()

    def venda(self):
        cod_prod = self.line_codprod.text()
        qtd_venda = self.line_qtd.text()
        vendedor = self.vendedor

        if cod_prod == "" or qtd_venda == "" or vendedor == "":
            self.msg_box.setStyleSheet("color: rgb(255, 0, 0);")
            self.msg_box.setText("Preencha Todos os campos!")

        try:
            venda_produto(cod_prod, qtd_venda, vendedor)
            self.msg_box.setStyleSheet("color: rgb(85, 255, 0);")
            self.msg_box.setText("Venda adicionada!")
            self.line_codprod.setText("")
            self.line_qtd.setText("")
            self.listar_venda()
        except:
            self.msg_box.setStyleSheet("color: rgb(255, 0, 0);")
            self.msg_box.setText("Produto Inexistente!")

    def listar_venda(self):
        cod_prod = self.line_codprod.text()
        vendedor = self.vendedor
        conn = sqlite3.connect("Vendas.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM '{vendedor}' WHERE vendedor = '{vendedor}'")
        produtos = cursor.fetchall()

        tela_principal.tw_saida.setRowCount(len(produtos))
        tela_principal.tw_saida.setColumnCount(6)

        for row, produto in enumerate(produtos):
            for col, value in enumerate(produto):
                item = QTableWidgetItem(str(value))
                tela_principal.tw_saida.setItem(row, col, item)
        conn.close()
        Tela_principal.listar_produtos


def iniciar_tela_cadastro():
    tela_login.close()
    tela_cadastro.show()


def logout():
    tela_login.show()
    tela_principal.close()


app = QApplication(sys.argv)
tela_saida = Tela_saida()
tela_principal = Tela_principal(tela_saida)
tela_login = Tela_login()
tela_cadastro = Tela_cadastro()


tela_login.pushButton_2.clicked.connect(iniciar_tela_cadastro)
tela_cadastro.pushButton.clicked.connect(Tela_cadastro.cadastrar_ui)
tela_login.pushButton.clicked.connect(Tela_login.login_ui)


if __name__ == "__main__":
    tela_login.show()
    app.exec_()
