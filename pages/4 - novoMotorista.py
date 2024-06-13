import streamlit as st
from util import cabEscala, tituloPage
import mysql.connector
from time import sleep
import datetime
from conexao import conexaoBD

st.set_page_config(
    "Motorista",
    layout="wide",
    initial_sidebar_state="collapsed"
)

conexao = conexaoBD()
mycursor = conexao.cursor()

sql = "SELECT * FROM motoristas_lista;"
mycursor.execute(sql)
dadosMotorista = mycursor.fetchall()

sql = """SELECT u.unidade, u.id_unidade, c.nome_cidade, c.id_cidades
    FROM unidades u
    LEFT JOIN motoristas_lista ml1 ON u.id_unidade = ml1.fgkey_unidade
    LEFT JOIN cidades_pontos c ON ml1.fgkey_cidade = c.id_cidades
    UNION
    SELECT u.unidade, u.id_unidade, c.nome_cidade, c.id_cidades
    FROM cidades_pontos c
    LEFT JOIN motoristas_lista ml2 ON c.id_cidades = ml2.fgkey_cidade
    LEFT JOIN unidades u ON ml2.fgkey_unidade = u.id_unidade;"""
mycursor.execute(sql)
cidadesUnidades = mycursor.fetchall()
unidades = list(set([x[0] for x in cidadesUnidades if x[0]]))
cidades = list(set([x[2] for x in cidadesUnidades if x[2]]))

sql = "SELECT * FROM funcao_motorista"
mycursor.execute(sql)
funcaoMot = mycursor.fetchall()

cabEscala()

if st.button("Voltar"):
    st.switch_page("pages/2 - Motoristas.py")

if len(st.query_params.to_dict()) != 0:
    st.write("acesso com parametro")
    pageFuncao = st.query_params["funcao"]
    idMot = st.query_params["id"]

    st.write(idMot)
    st.write(pageFuncao)
    if pageFuncao == "editar":
        tituloPage("Editar Motorista")

        with st.form("motorista", clear_on_submit=True, border=False):
            col1, col2 = st.columns([3, 1])
            with col1:
                nome = st.text_input("Nome", [x[1] for x in dadosMotorista if str(x[0]) == str(idMot)][0])
            with col2:
                matricula = st.text_input("Matrícula", [x[7] for x in dadosMotorista if str(x[0]) == str(idMot)][0])

            col1, col2 = st.columns(2)
            with col1:
                unidParam = next(x[5] for x in dadosMotorista if str(x[0]) == str(idMot))
                nomeUnid = next(x[0] for x in cidadesUnidades if x[1] == unidParam)
                idxUnid = unidades.index(str(nomeUnid))
                unidade = st.selectbox("Unidade", unidades, idxUnid, placeholder="")
                if unidade:
                    idUnid = list(set([x[1] for x in cidadesUnidades if x[0] == unidade]))[0]
                else:
                    idUnid = "NULL"
            with col2:
                cidParam = next(x[6] for x in dadosMotorista if str(x[0]) == str(idMot))
                nomeCid = next(x[2] for x in cidadesUnidades if x[3] == cidParam)
                idxCid = cidades.index(str(nomeCid))
                cidade = st.selectbox("Cidade de Origem", cidades, idxCid, placeholder="")
                if cidade:
                    idCid = list(set([x[3] for x in cidadesUnidades if x[2] == cidade]))[0]
                else:
                    idCid = "NULL"

            col1, col2, col3 = st.columns(3)
            with col1:
                funcParam = next(x[2] for x in dadosMotorista if str(x[0]) == str(idMot))
                nomeFunc = next(x[1] for x in funcaoMot if x[0] == funcParam)
                idxFunc = list(set([x[1] for x in funcaoMot if x[1]])).index(str(nomeFunc))
                funcao = st.selectbox("Função", list(set([x[1] for x in funcaoMot if x[1]])), idxFunc, placeholder="")
                if funcao:
                    idFuncao = list(set([x[0] for x in funcaoMot if x[1] == funcao]))[0]
                else:
                    idFuncao = "NULL"
            with col2:
                dtAdmissao = st.date_input("Data de Admissão", next(x[3] for x in dadosMotorista if str(x[0]) == str(idMot)), format="DD/MM/YYYY")
            with col3:
                status = st.selectbox("Status", ["Inativo", "Ativo"], next(x[4] for x in dadosMotorista if str(x[0]) == str(idMot)))
                status = 1 if status == "Ativo" else 0

            colLiv, colBt = st.columns([5, 1])
            with colBt:
                st.write("")
                salvar = st.form_submit_button("Salvar", use_container_width=True)

            if salvar:
                dadosMot = {
                    "id": int(idMot),
                    "nome": nome.upper(),
                    "matricula": matricula,
                    "unidade": idUnid,
                    "cidade": idCid,
                    "funcao": idFuncao,
                    "admissao": dtAdmissao.strftime("%Y-%m-%d"),
                    "status": status
                }

                sql = "UPDATE motoristas_lista SET nome_motorista = %(nome)s, fgkey_funcao = %(funcao)s, data_admissao = %(admissao)s, status_motorista = %(status)s, fgkey_unidade = %(unidade)s, fgkey_cidade = %(cidade)s, matricula_motorista = %(matricula)s WHERE id_mot = %(id)s;"
                mycursor.execute(sql, dadosMot)
                conexao.commit()

                mycursor.close()
                conexao.close()

                st.toast("Motorista atualizado com sucesso!", icon="✅")
                sleep(1)
                st.switch_page("pages/2 - Motoristas.py")
else:
    tituloPage("Cadastrar Motorista")

    with st.form("motorista", clear_on_submit=True, border=False):
        col1, col2 = st.columns([3, 1])
        with col1:
            nome = st.text_input("Nome")
        with col2:
            matricula = st.text_input("Matrícula")

        col1, col2 = st.columns(2)
        with col1:
            unidade = st.selectbox("Unidade", unidades, None, placeholder="")
            if unidade:
                idUnid = list(set([x[1] for x in cidadesUnidades if x[0] == unidade]))[0]
            else:
                idUnid = "NULL"
        with col2:
            cidade = st.selectbox("Cidade de Origem", cidades, None, placeholder="")
            if cidade:
                idCid = list(set([x[3] for x in cidadesUnidades if x[2] == cidade]))[0]
            else:
                idCid = "NULL"

        col1, col2, col3 = st.columns(3)
        with col1:
            funcao = st.selectbox("Função", list(set([x[1] for x in funcaoMot if x[1]])), None, placeholder="")
            if funcao:
                idFuncao = list(set([x[0] for x in funcaoMot if x[1] == funcao]))[0]
            else:
                idFuncao = "NULL"
        with col2:
            dtAdmissao = st.date_input("Data de Admissão", format="DD/MM/YYYY")
        with col3:
            status = st.selectbox("Status", ["Ativo", "Inativo"])
            status = 1 if status == "Ativo" else 0

        colLiv, colBt = st.columns([5, 1])
        with colBt:
            st.write("")
            salvar = st.form_submit_button("Salvar", use_container_width=True)

        if salvar:
            dadosMot = {
                "nome": nome.upper(),
                "matricula": matricula,
                "unidade": idUnid,
                "cidade": idCid,
                "funcao": idFuncao,
                "admissao": dtAdmissao.strftime("%Y-%m-%d"),
                "status": status
            }

            sql = "INSERT INTO motoristas_lista VALUES('NULL', %(nome)s, %(funcao)s, %(admissao)s, %(status)s, %(unidade)s, %(cidade)s, %(matricula)s);"
            mycursor.execute(sql, dadosMot)
            conexao.commit()

            mycursor.close()
            conexao.close()

            st.toast("Motorista cadastrado com sucesso!", icon="✅")
            sleep(1)
            st.switch_page("pages/2 - Motoristas.py")

mycursor.close()
conexao.close()