# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Produtos_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaMain(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(919, 644)
        MainWindow.setStyleSheet("background-color: rgb(106, 106, 106);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_home = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_home.setFont(font)
        self.btn_home.setStyleSheet(
            "QPushButton{\n"
            "text-decoration: none;\n"
            "border: none;\n"
            "padding: 12px 40px;\n"
            "font-size: 16px;\n"
            "background-color: gray;\n"
            "color: #fff;\n"
            "border-radius: 5px;\n"
            "box-shadow: 7px 6px 28px 1px rgba(0, 0, 0, 0.24);\n"
            "cursor: pointer;\n"
            "outline: none;\n"
            "transition: 0.2s all;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "text-decoration: none;\n"
            "border: none;\n"
            "padding: 12px 40px;\n"
            "font-size: 16px;\n"
            "background-color: rgb(99, 99, 99);\n"
            "color: #fff;\n"
            "border-radius: 5px;\n"
            "box-shadow: 7px 6px 28px 1px rgba(0, 0, 0, 0.24);\n"
            "cursor: pointer;\n"
            "outline: none;\n"
            "transition: 0.2s all;\n"
            "}\n"
            ""
        )
        self.btn_home.setObjectName("btn_home")
        self.horizontalLayout.addWidget(self.btn_home)
        self.btn_produtos = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_produtos.setFont(font)
        self.btn_produtos.setStyleSheet(
            "QPushButton{\n"
            "text-decoration: none;\n"
            "border: none;\n"
            "padding: 12px 40px;\n"
            "font-size: 16px;\n"
            "background-color: gray;\n"
            "color: #fff;\n"
            "border-radius: 5px;\n"
            "box-shadow: 7px 6px 28px 1px rgba(0, 0, 0, 0.24);\n"
            "cursor: pointer;\n"
            "outline: none;\n"
            "transition: 0.2s all;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "text-decoration: none;\n"
            "border: none;\n"
            "padding: 12px 40px;\n"
            "font-size: 16px;\n"
            "background-color: rgb(99, 99, 99);\n"
            "color: #fff;\n"
            "border-radius: 5px;\n"
            "box-shadow: 7px 6px 28px 1px rgba(0, 0, 0, 0.24);\n"
            "cursor: pointer;\n"
            "outline: none;\n"
            "transition: 0.2s all;\n"
            "}\n"
            ""
        )
        self.btn_produtos.setObjectName("btn_produtos")
        self.horizontalLayout.addWidget(self.btn_produtos)
        self.btn_venda = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_venda.setFont(font)
        self.btn_venda.setStyleSheet(
            "QPushButton{\n"
            "text-decoration: none;\n"
            "border: none;\n"
            "padding: 12px 40px;\n"
            "font-size: 16px;\n"
            "background-color: gray;\n"
            "color: #fff;\n"
            "border-radius: 5px;\n"
            "box-shadow: 7px 6px 28px 1px rgba(0, 0, 0, 0.24);\n"
            "cursor: pointer;\n"
            "outline: none;\n"
            "transition: 0.2s all;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "text-decoration: none;\n"
            "border: none;\n"
            "padding: 12px 40px;\n"
            "font-size: 16px;\n"
            "background-color: rgb(99, 99, 99);\n"
            "color: #fff;\n"
            "border-radius: 5px;\n"
            "box-shadow: 7px 6px 28px 1px rgba(0, 0, 0, 0.24);\n"
            "cursor: pointer;\n"
            "outline: none;\n"
            "transition: 0.2s all;\n"
            "}\n"
            ""
        )
        self.btn_venda.setObjectName("btn_venda")
        self.horizontalLayout.addWidget(self.btn_venda)
        self.btn_logout = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_logout.setFont(font)
        self.btn_logout.setStyleSheet(
            "QPushButton{\n"
            "text-decoration: none;\n"
            "border: none;\n"
            "padding: 12px 40px;\n"
            "font-size: 16px;\n"
            "background-color: gray;\n"
            "color: #fff;\n"
            "border-radius: 5px;\n"
            "box-shadow: 7px 6px 28px 1px rgba(0, 0, 0, 0.24);\n"
            "cursor: pointer;\n"
            "outline: none;\n"
            "transition: 0.2s all;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "text-decoration: none;\n"
            "border: none;\n"
            "padding: 12px 40px;\n"
            "font-size: 16px;\n"
            "background-color: rgb(99, 99, 99);\n"
            "color: #fff;\n"
            "border-radius: 5px;\n"
            "box-shadow: 7px 6px 28px 1px rgba(0, 0, 0, 0.24);\n"
            "cursor: pointer;\n"
            "outline: none;\n"
            "transition: 0.2s all;\n"
            "}\n"
            ""
        )
        self.btn_logout.setObjectName("btn_logout")
        self.horizontalLayout.addWidget(self.btn_logout)
        self.verticalLayout_2.addWidget(self.frame)
        self.Pages = QtWidgets.QStackedWidget(self.centralwidget)
        self.Pages.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.Pages.setObjectName("Pages")
        self.pg_table = QtWidgets.QWidget()
        self.pg_table.setObjectName("pg_table")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.pg_table)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(self.pg_table)
        self.tabWidget.setObjectName("tabWidget")
        self.tables = QtWidgets.QWidget()
        self.tables.setObjectName("tables")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tables)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txt_file = QtWidgets.QLineEdit(self.tables)
        self.txt_file.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius:10px;"
        )
        self.txt_file.setMaxLength(2000)
        self.txt_file.setObjectName("txt_file")
        self.horizontalLayout_2.addWidget(self.txt_file)
        self.btn_open = QtWidgets.QPushButton(self.tables)
        self.btn_open.setObjectName("btn_open")
        self.horizontalLayout_2.addWidget(self.btn_open)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.tables)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.tw_estoque = QtWidgets.QTreeWidget(self.tables)
        self.tw_estoque.setObjectName("tw_estoque")
        self.verticalLayout_5.addWidget(self.tw_estoque)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.tables)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.tw_saida = QtWidgets.QTreeWidget(self.tables)
        self.tw_saida.setObjectName("tw_saida")
        self.verticalLayout_4.addWidget(self.tw_saida)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.frame_2 = QtWidgets.QFrame(self.tables)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_atualizar = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_atualizar.setFont(font)
        self.btn_atualizar.setStyleSheet(
            "QPushButton{\n"
            "text-decoration: none;\n"
            "border: none;\n"
            "padding: 12px 40px;\n"
            "font-size: 16px;\n"
            "background-color: gray;\n"
            "color: #fff;\n"
            "border-radius: 5px;\n"
            "box-shadow: 7px 6px 28px 1px rgba(0, 0, 0, 0.24);\n"
            "cursor: pointer;\n"
            "outline: none;\n"
            "transition: 0.2s all;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "text-decoration: none;\n"
            "border: none;\n"
            "padding: 12px 40px;\n"
            "font-size: 16px;\n"
            "background-color: rgb(99, 99, 99);\n"
            "color: #fff;\n"
            "border-radius: 5px;\n"
            "box-shadow: 7px 6px 28px 1px rgba(0, 0, 0, 0.24);\n"
            "cursor: pointer;\n"
            "outline: none;\n"
            "transition: 0.2s all;\n"
            "}\n"
            ""
        )
        self.btn_atualizar.setObjectName("btn_atualizar")
        self.verticalLayout_3.addWidget(self.btn_atualizar)
        self.btn_gerar = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_gerar.setFont(font)
        self.btn_gerar.setStyleSheet(
            "QPushButton{\n"
            "text-decoration: none;\n"
            "border: none;\n"
            "padding: 12px 40px;\n"
            "font-size: 16px;\n"
            "background-color: gray;\n"
            "color: #fff;\n"
            "border-radius: 5px;\n"
            "box-shadow: 7px 6px 28px 1px rgba(0, 0, 0, 0.24);\n"
            "cursor: pointer;\n"
            "outline: none;\n"
            "transition: 0.2s all;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "text-decoration: none;\n"
            "border: none;\n"
            "padding: 12px 40px;\n"
            "font-size: 16px;\n"
            "background-color: rgb(99, 99, 99);\n"
            "color: #fff;\n"
            "border-radius: 5px;\n"
            "box-shadow: 7px 6px 28px 1px rgba(0, 0, 0, 0.24);\n"
            "cursor: pointer;\n"
            "outline: none;\n"
            "transition: 0.2s all;\n"
            "}\n"
            ""
        )
        self.btn_gerar.setObjectName("btn_gerar")
        self.verticalLayout_3.addWidget(self.btn_gerar)
        self.btn_estorno = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_estorno.setFont(font)
        self.btn_estorno.setStyleSheet(
            "QPushButton{\n"
            "text-decoration: none;\n"
            "border: none;\n"
            "padding: 12px 40px;\n"
            "font-size: 16px;\n"
            "background-color: gray;\n"
            "color: #fff;\n"
            "border-radius: 5px;\n"
            "box-shadow: 7px 6px 28px 1px rgba(0, 0, 0, 0.24);\n"
            "cursor: pointer;\n"
            "outline: none;\n"
            "transition: 0.2s all;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "text-decoration: none;\n"
            "border: none;\n"
            "padding: 12px 40px;\n"
            "font-size: 16px;\n"
            "background-color: rgb(99, 99, 99);\n"
            "color: #fff;\n"
            "border-radius: 5px;\n"
            "box-shadow: 7px 6px 28px 1px rgba(0, 0, 0, 0.24);\n"
            "cursor: pointer;\n"
            "outline: none;\n"
            "transition: 0.2s all;\n"
            "}\n"
            ""
        )
        self.btn_estorno.setObjectName("btn_estorno")
        self.verticalLayout_3.addWidget(self.btn_estorno)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tables, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_8.addWidget(self.tabWidget)
        self.Pages.addWidget(self.pg_table)
        self.pg_venda = QtWidgets.QWidget()
        self.pg_venda.setObjectName("pg_venda")
        self.label_4 = QtWidgets.QLabel(self.pg_venda)
        self.label_4.setGeometry(QtCore.QRect(300, 200, 321, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.Pages.addWidget(self.pg_venda)
        self.pg_home = QtWidgets.QWidget()
        self.pg_home.setObjectName("pg_home")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.pg_home)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.pg_home)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Pages.addWidget(self.pg_home)
        self.verticalLayout_2.addWidget(self.Pages)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Produtos"))
        self.btn_home.setText(_translate("MainWindow", "Home"))
        self.btn_produtos.setText(_translate("MainWindow", "Produtos"))
        self.btn_venda.setText(_translate("MainWindow", "Venda"))
        self.btn_logout.setText(_translate("MainWindow", "LogOut"))
        self.btn_open.setText(_translate("MainWindow", "Abrir"))
        self.label_3.setText(_translate("MainWindow", "Estoque"))
        self.tw_estoque.headerItem().setText(
            0, _translate("MainWindow", "Nome Produto")
        )
        self.tw_estoque.headerItem().setText(1, _translate("MainWindow", "Estoque"))
        self.tw_estoque.headerItem().setText(2, _translate("MainWindow", "Valor R$"))
        self.label_2.setText(_translate("MainWindow", "Saida"))
        self.tw_saida.headerItem().setText(0, _translate("MainWindow", "Produto"))
        self.tw_saida.headerItem().setText(1, _translate("MainWindow", "Valor"))
        self.tw_saida.headerItem().setText(2, _translate("MainWindow", "Quantidade"))
        self.tw_saida.headerItem().setText(3, _translate("MainWindow", "Usuario"))
        self.btn_atualizar.setToolTip(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center">Importar</p></body></html>',
            )
        )
        self.btn_atualizar.setText(_translate("MainWindow", "Atualizar"))
        self.btn_gerar.setToolTip(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center">Importar</p></body></html>',
            )
        )
        self.btn_gerar.setText(_translate("MainWindow", "Gerar Saida"))
        self.btn_estorno.setToolTip(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center">Importar</p></body></html>',
            )
        )
        self.btn_estorno.setText(_translate("MainWindow", "Estorno"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tables), _translate("MainWindow", "TreeWidget")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2")
        )
        self.label_4.setText(_translate("MainWindow", "Vendas"))
        self.label.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:48pt; font-weight:600;">Ryan\'s Company</span></p><p align="center"><span style=" font-size:28pt; font-weight:600;">Sistema de gerenciamento</span></p></body></html>',
            )
        )
