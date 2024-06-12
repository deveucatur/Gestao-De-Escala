import mysql.connector

def conexaoBD():
    conexao = mysql.connector.connect(
        passwd='',
        port=3306,
        user='root',
        host='localhost',
        database='gestao_escala'
    )

    return conexao