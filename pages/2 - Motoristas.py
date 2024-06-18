import streamlit as st
from util import cabEscala, tabelas, tituloPage, excluirMotorista, sideBar, ativarMotorista
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

colAux, colBt = st.columns([4, 1])

with colBt:
    novoMot = st.button("Novo Motorista", use_container_width=True)

if novoMot:
    st.switch_page("pages/4 - novoMotorista.py")

tituloPage("Dados dos Motoristas")

@st.experimental_fragment
def fragTabela(dadosMotorista):
    with st.expander("Filtrar"):
        filNome = st.text_input("Nome", placeholder="Filtrar por nome")
        if filNome:
            dadosMotorista = [x for x in dadosMotorista if filNome.upper() in x[1]]
        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            unidades = list(set(x[8] for x in dadosMotorista if x[8]))
            filUnidade = st.multiselect("Unidades", unidades, placeholder="Selecionar unidades")
            if filUnidade:
                dadosMotorista = [x for x in dadosMotorista if x[8] in filUnidade]

        with col2:
            cidades = list(set(x[9] for x in dadosMotorista if x[9]))
            filCidade = st.multiselect("Cidades de Origem", cidades, placeholder="Selecionar cidades")
            if filCidade:
                dadosMotorista = [x for x in dadosMotorista if x[9] in filCidade]

        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            funcoes = list(set(x[10] for x in dadosMotorista if x[10]))
            filFuncao = st.multiselect("Funções", funcoes, placeholder="Selecionar funções")
            if filFuncao:
                dadosMotorista = [x for x in dadosMotorista if x[10] in filFuncao]
        with col2:
            situacoes = list({"Escalado" for x in dadosMotorista if x[11]})
            setSituacoes = set()
            for subLista in (x[12].split("~/>") for x in dadosMotorista if x[12]):
                setSituacoes.update(subLista)
            if any(not x[11] and not x[12] for x in dadosMotorista):
                situacoes.append("Livre")
            situacoes += list(setSituacoes)
            filSituacao = st.multiselect("Situações", situacoes, placeholder="Selecionar situações")
            if filSituacao:
                dadosMotorista = [x for x in dadosMotorista if (("Escalado" in filSituacao and x[11]) or any(y in x[12].split("~/>") for y in filSituacao if x[12]) or ("Livre" in filSituacao and not x[11] and not x[12]))]
        with col3:
            status = st.radio("Status", ["Ativo", "Inativo"], horizontal=True)
            if status == "Ativo":
                dadosMotorista = [x for x in dadosMotorista if x[4] == 1]
            else:
                dadosMotorista = [x for x in dadosMotorista if x[4] == 0]
    if len(dadosMotorista) != 0:
        if status == "Ativo":
            tabelas("MotoristaAtivo", dadosMotorista)
        elif status == "Inativo":
            tabelas("MotoristaInativo", dadosMotorista)
    else:
        st.info("Nenhum motorista encontrado")

fragTabela(dadosMotorista)

if len(st.query_params.to_dict()) != 0:
    pageFuncao = st.query_params["funcao"]
    idMot = st.query_params["id"]
    nomeMot = next(x[1] for x in dadosMotorista if str(x[0]) == str(idMot))
    matricMot = next(x[7] for x in dadosMotorista if str(x[0]) == str(idMot))

    if pageFuncao == "excluir":
        excluirMotorista(idMot, nomeMot, matricMot)
    elif pageFuncao == "ativar":
        ativarMotorista(idMot, nomeMot, matricMot)