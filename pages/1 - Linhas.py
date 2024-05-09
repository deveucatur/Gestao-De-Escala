import streamlit as st
import json
import pandas as pd
import plotly.express as px
from util import cabecalho

st.set_page_config(
    "Linhas",
    layout="wide",
    initial_sidebar_state="collapsed"
)

cabecalho("Rahyan")

with open("documentos/projeto_linhas_horarios.json", "r", encoding="utf-8") as file:
    data = json.load(file)

opcoes = []
for key, value in data.items():
    linha = value["LINHA"]
    opcoes.append((f"{key} - {linha}", key))

linhaSelect = st.multiselect("Linhas", opcoes, format_func=lambda x: x[0], placeholder="Escolha as linhas que deseja visualizar")

if len(linhaSelect) != 0:
    tasks = []
    for linhaChave in linhaSelect:
        if linhaChave[1] in data:
            linha_data = data[linhaChave[1]]
            linha = linha_data['LINHA']
            for direcao, direcao_data in linha_data['PERCURSO'].items():
                paradas = list(direcao_data.values())
                for i in range(len(paradas) - 1):
                    parada_atual = paradas[i]
                    prox_parada = paradas[i + 1]
                    tasks.append({
                        'Linha': linha,
                        'Direcao': direcao,
                        'Parada': parada_atual['SECCIONAMENTO'],
                        'Hora_Inicio': parada_atual['HORÁRIO SAIDA'],
                        'Hora_Fim': prox_parada['HORÁRIO CHEGADA'],
                        'Intervalo_Inicio': parada_atual['HORÁRIO CHEGADA'],
                        'Intervalo_fim': parada_atual['HORÁRIO SAIDA']
                    })

    df = pd.DataFrame(tasks)

    df['Hora_Inicio'] = pd.to_datetime(df['Hora_Inicio'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
    df['Hora_Fim'] = pd.to_datetime(df['Hora_Fim'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

    df['Duração'] = df['Hora_Fim'] - df['Hora_Inicio']

    df = df.dropna(subset=['Hora_Inicio', 'Hora_Fim'])

    if not df.empty:
        df['Intervalo'] = df['Hora_Fim'] - df['Hora_Inicio']

        df['Intervalo_Segundos'] = df['Intervalo'].dt.total_seconds()

        fig = px.timeline(df, x_start='Hora_Inicio', x_end='Hora_Fim', y='Linha', color='Direcao', title='Gráfico Gantt de Linhas de Ônibus', width=1250, labels={'Hora_Inicio': 'Horário de Saída', 'Hora_Fim': 'Horário de Chegada'})

        st.plotly_chart(fig)
    else:
        st.warning("Nenhuma linha selecionada. Por favor, escolha as linhas que deseja visualizar.")

def semana_by_number(string_sem):
    string_sem = str(string_sem).strip()
    aux = {'0': "Seg",
           '1': "Ter",
           '2': "Qua",
           '3': "Qui",
           '4': "Sex",
           '5': "Sáb",
           '6': "Dom"}
    
    if string_sem in aux.keys():
        retorno = aux[string_sem]
    else:
        retorno = None

    return retorno

for linhaChave in linhaSelect:
    dadoLinha = data[linhaChave[1]]

    st.title(linhaChave[0])
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f'Horário de Início: {dadoLinha["HORÁRIO INÍCIO"]}')
    with col2:
        st.subheader(f'Frequência: {semana_by_number(dadoLinha["FREQUÊNCIA"][0])}')

    col1, col2, col3 = st.columns([5, 2, 5])
    with col1:
        st.write("---")
    with col2:
        st.subheader("Percurso (Volta)")
    with col3:
        st.write("---")

    for subChave, subValor in dadoLinha["PERCURSO"]["Volta"].items():
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text_input("Código", subChave, key=f'VOLTA: Chave - {subChave} | {subValor} | {linhaChave}', disabled=True)
        with col2:
            st.text_input("Seccionamento", subValor["SECCIONAMENTO"], key=f'VOLTA: sec - {subChave} | {subValor["SECCIONAMENTO"]} | {linhaChave}', disabled=True)
        with col3:
            st.text_input("Horário de Chegada", subValor["HORÁRIO CHEGADA"], key=f'VOLTA: che - {subChave} | {subValor["HORÁRIO CHEGADA"]} | {linhaChave}', disabled=True)
        with col4:
            st.text_input("Tempo de Parada", subValor["TEMPO DE PARADA"], key=f'VOLTA: par - {subChave} | {subValor["TEMPO DE PARADA"]} | {linhaChave}', disabled=True)
        with col5:
            st.text_input("Horário de Saída", subValor["HORÁRIO SAIDA"], key=f'VOLTA: sai - {subChave} | {subValor["HORÁRIO SAIDA"]} | {linhaChave}', disabled=True)

    col1, col2, col3 = st.columns([5.5, 2, 5.5])
    with col1:
        st.write("---")
    with col2:
        st.subheader("Percurso (Ida)")
    with col3:
        st.write("---")

    if "Ida" in dadoLinha["PERCURSO"]:
        for subChave, subValor in dadoLinha["PERCURSO"]["Ida"].items():
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text_input("Código", subChave, key=f'IDA: Chave - {subChave} | {subValor} | {linhaChave}', disabled=True)
            with col2:
                st.text_input("Seccionamento", subValor["SECCIONAMENTO"], key=f'IDA: sec - {subChave} | {subValor["SECCIONAMENTO"]} | {linhaChave}', disabled=True)
            with col3:
                st.text_input("Horário de Chegada", subValor["HORÁRIO CHEGADA"], key=f'IDA: che - {subChave} | {subValor["HORÁRIO CHEGADA"]} | {linhaChave}', disabled=True)
            with col4:
                st.text_input("Tempo de Parada", subValor["TEMPO DE PARADA"], key=f'IDA: par - {subChave} | {subValor["TEMPO DE PARADA"]} | {linhaChave}', disabled=True)
            with col5:
                st.text_input("Horário de Saída", subValor["HORÁRIO SAIDA"], key=f'IDA: sai - {subChave} | {subValor["HORÁRIO SAIDA"]} | {linhaChave}', disabled=True)
    else:
        st.info("Não há dados de 'Ida' para esta linha.")
    st.write("---")