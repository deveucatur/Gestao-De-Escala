import streamlit as st
from util import cabEscala

st.set_page_config(
    "Configurações",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# cabecalho("Rahyan")
cabEscala()

st.title("Configurações")
