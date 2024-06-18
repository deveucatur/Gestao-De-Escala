import mysql.connector

def conexaoBD():
    conexao = mysql.connector.connect(
        passwd='6Kp62muMRD@!1',
        port=3307,
        user='root',
        host='192.168.0.7',
        database='gestao_escala'
    )

    return conexao