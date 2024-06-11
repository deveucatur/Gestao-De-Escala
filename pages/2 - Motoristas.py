import streamlit as st
import pandas as pd
from util import cabEscala

st.set_page_config(
    "Motoristas",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# cabecalho("Rahyan")
cabEscala()

colAux, colBt = st.columns([4, 1])

with colBt:
    novoMot = st.button("Novo Motorista", use_container_width=True)

if novoMot:
    st.switch_page("pages/4 - novoMotorista.py")

st.title("Dados dos Motoristas")

planil = pd.read_excel('documentos/ProjetoMotoristas.xlsx', sheet_name='listaMotoristas')

columns_plan = [column for column in planil]

listMotoristas = []

for idx_mot in range(len(planil['ANO'])):
    aux_list = [planil[colm][idx_mot] for colm in columns_plan]
    
    listMotoristas.append(aux_list)

rotulos = ["ANO", "EMPRESA", "CHAPA", "NOME", "FUNÇÃO", "GRUPO", "CEEMs", "CIDADE", "ÁREA", "DATA ADMISSÃO", "ATIVO"]

# st.write(listMotoristas)

df = pd.DataFrame(listMotoristas, columns=rotulos)

st.table(df)