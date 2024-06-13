import streamlit as st
from util import cabEscala, tabelas, tituloPage, excluirMotorista, sideBar
from conexao import conexaoBD
from datetime import datetime

st.set_page_config(
    "Motoristas - EscalaMax",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="https://raw.githubusercontent.com/RahyanRamos/Imagens.Eucatur/main/logoIcon-EscalaMax.png"
)

conexao = conexaoBD()
mycursor = conexao.cursor()

cabEscala()
sideBar()

hoje = datetime.today().date().strftime("%Y-%m-%d")
sql = f"""SELECT 
        *,
        (
            SELECT 
                unidade
            FROM
                unidades
            WHERE 
                id_unidade = motoristas_lista.fgkey_unidade
        ),
        (
            SELECT 
                nome_cidade
            FROM
                cidades_pontos
            WHERE 
                id_cidades = motoristas_lista.fgkey_cidade
        ),
        (
            SELECT 
                nome_funcao
            FROM
                funcao_motorista
            WHERE
                id_funcao = motoristas_lista.fgkey_funcao
        ),
        (
            SELECT 
                GROUP_CONCAT(id_viagem SEPARATOR '~/>')
            FROM 
                registro_viagens_mot
            WHERE 
                motorista_fgkey = motoristas_lista.id_mot 
                AND data_ini <= '{hoje}' AND data_fim >= '{hoje}'
        ),
        (
            SELECT 
                GROUP_CONCAT(motivo SEPARATOR '~/>')
            FROM 
                motivo_ausencia
            WHERE 
                id_motivo IN (SELECT 
                        motivo_fgkey
                    FROM 
                        motoristas_ausencia
                    WHERE 
                        motorista_fgkey = motoristas_lista.id_mot
                        AND data_ini <= '{hoje}' AND data_fim >= '{hoje}')
        )
    FROM 
        motoristas_lista"""
mycursor.execute(sql)
dadosMotorista = mycursor.fetchall()

# st.write(dadosMotorista)

colAux, colBt = st.columns([4, 1])

with colBt:
    novoMot = st.button("Novo Motorista", use_container_width=True)

if novoMot:
    st.switch_page("pages/4 - novoMotorista.py")

tituloPage("Dados dos Motoristas")

tabelas("Motorista", dadosMotorista)

if len(st.query_params.to_dict()) != 0:
    pageFuncao = st.query_params["funcao"]
    idMot = st.query_params["id"]
    nomeMot = next(x[1] for x in dadosMotorista if str(x[0]) == str(idMot))
    matricMot = next(x[7] for x in dadosMotorista if str(x[0]) == str(idMot))

    if pageFuncao == "excluir":
        excluirMotorista(idMot, nomeMot, matricMot)