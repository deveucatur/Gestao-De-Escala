import streamlit as st
from util import cabEscala

st.set_page_config(
    "Configurações - EscalaMax",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="https://raw.githubusercontent.com/RahyanRamos/Imagens.Eucatur/main/logoIcon-EscalaMax.png"
)

cabEscala()

st.title("Configurações")
