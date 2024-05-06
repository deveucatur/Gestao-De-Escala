import streamlit as st

st.set_page_config(
    "Escalas",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("Gestão de Escalas")

col1, col2, col3, col4 = st.columns(4)

with col1:
    btLinha = st.button("Escala de Linhas", use_container_width=True)
    if btLinha:
        st.switch_page("pages/1 - Linhas.py")
with col2:
    btMotorista = st.button("Escala de Motoristas", use_container_width=True)
    if btMotorista:
        st.switch_page("pages/2 - Motoristas.py")
with col3:
    btEscala = st.button("Programação de Escalas", use_container_width=True)
    if btEscala:
        st.switch_page("pages/3 - Escalas.py")
with col4:
    btConfig = st.button("Configurações", use_container_width=True)
    if btConfig:
        st.switch_page("pages/99 - Configurações.py")