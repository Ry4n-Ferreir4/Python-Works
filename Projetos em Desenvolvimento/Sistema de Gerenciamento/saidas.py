import sqlite3
import pandas as pd

import random
import datetime

data_atual = datetime.date.today()


def gerar_id_venda():
    id_venda = random.randint(10000, 99999)
    return id_venda


def venda_produto(cod_prod, quantidade_venda, vendedor):
    banco_estoque = sqlite3.connect("Estoque.db")
    cursor_estoque = banco_estoque.cursor()

    banco_vendas = sqlite3.connect("Vendas.db")
    cursor_vendas = banco_vendas.cursor()
    cursor_vendas.execute(
        f"CREATE TABLE IF NOT EXISTS {vendedor} (IDVenda INTEGER PRIMARY KEY, Produto TEXT, Valor REAL,Quantidade INTEGER, Vendedor TEXT,Data TEXT)"
    )

    cursor_estoque.execute(f"SELECT qtdprod FROM produtos WHERE Codprod = '{cod_prod}'")
    qtd_prod_db = cursor_estoque.fetchall()

    cursor_estoque.execute(f"SELECT preco FROM produtos WHERE Codprod = '{cod_prod}'")
    preco_produto_db = cursor_estoque.fetchall()

    cursor_estoque.execute(f"SELECT nome FROM produtos WHERE Codprod = '{cod_prod}'")
    produto_db = cursor_estoque.fetchall()

    preco_produto_int = int(preco_produto_db[0][0])
    quantidade_venda_int = int(quantidade_venda)
    qtd_prod_int = int(qtd_prod_db[0][0])
    produto_str = produto_db[0][0]
    id_existe_db = "0"
    id_venda = gerar_id_venda()
    valor_da_venda = preco_produto_int * quantidade_venda_int
    data = data_atual.strftime("%d/%m/%Y")

    """while id_venda == id_existe_db:
        id_venda = gerar_id_venda()"""

    if quantidade_venda_int > qtd_prod_int:
        print("Produtos Insuficintes")
    else:
        query_venda = f"INSERT INTO {vendedor} (IDVenda, Produto, Valor, Quantidade, Vendedor, Data) VALUES (?, ?, ?, ?, ?, ?)"
        values = (
            id_venda,
            produto_str,
            valor_da_venda,
            quantidade_venda_int,
            vendedor,
            data,
        )

        cursor_vendas.execute(query_venda, values)
        banco_vendas.commit()
        banco_vendas.close()

        query = "UPDATE produtos SET qtdprod = qtdprod - ? WHERE Codprod = ?"
        cursor_estoque.execute(query, (quantidade_venda_int, cod_prod))
        banco_estoque.commit()
        banco_estoque.close()
