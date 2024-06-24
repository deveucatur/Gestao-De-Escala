import streamlit as st
from util import cabEscala, botaoHome, sideBar

st.set_page_config(
    "EscalaMax",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="https://raw.githubusercontent.com/RahyanRamos/Imagens.Eucatur/main/logoIcon-EscalaMax.png"
)

cabEscala()
sideBar()

col1, col2, col3, col4 = st.columns(4)

with col1:
    botaoHome("Linhas", "https://cdn-icons-png.flaticon.com/128/646/646018.png", "http://localhost:8501/Linhas")
with col2:
    botaoHome("Motoristas", "https://cdn-icons-png.flaticon.com/128/5283/5283024.png", "http://localhost:8501/Motoristas")
with col3:
    botaoHome("Escalas", "https://cdn-icons-png.flaticon.com/128/1050/1050608.png", "http://localhost:8501/Escalas")
with col4:
    botaoHome("Configurações", "https://cdn-icons-png.flaticon.com/128/1658/1658993.png", "http://localhost:8501/Configura%C3%A7%C3%B5es")

# st.text_input("Texto teste", placeholder="Place Holder Teste")
# st.text_input("teste de css nativo")
# st.selectbox("select teste", ["teste1", "teste 2"])
# st.text_area("teste")
# st.checkbox("teste")