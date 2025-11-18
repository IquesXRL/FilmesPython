import sqlite3
import pandas as pd


# 1 - Função de conexão
def conecta_bd():
    conn = sqlite3.connect('titulo.db')
    return conn

# 2 - Inserir Dados
def insere_dados(nome,ano,nota):
    conn = conecta_bd()
    cursor = conn.cursor()
    cursor.execute(
            """
      INSERT INTO filmes(nome,ano,nota)
      VALUES(?, ?, ?) 
""",(nome,ano,nota)
    )
    conn.commit()
    conn.close()

# 3 - Listagem de dados
def obter_dados():
    conn = conecta_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM filmes")
    dados = cursor.fetchall()
    cursor.close()

    colunas = ["id", "nome", "ano", "nota"]
    return pd.DataFrame(dados, columns=colunas)

def deletar_dados(id_filme):
    conn = conecta_bd()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM filmes WHERE id = ?", (id_filme,))
    conn.commit()
    conn.close()


def view_dados(id_filme):
    conn = conecta_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM filmes WHERE id = ?", (id_filme,))
    dados = cursor.fetchone()
    cursor.close()

    if not dados:
        return None

    colunas = ["id", "nome", "ano", "nota"]
    return dict(zip(colunas, dados))