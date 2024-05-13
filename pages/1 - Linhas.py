import streamlit as st
import json
from util import cabecalho
from datetime import timedelta, date, datetime


st.set_page_config(
    "Linhas",
    layout="wide",
    initial_sidebar_state="collapsed"
)

cabecalho("Rahyan")
with open("documentos/projeto_linhas_horarios.json", "r", encoding="utf-8") as file:
    linhas_dados = json.load(file)


def time_by_min(time):
    return (time.hour*60)+time.minute


def diferenca_minutos_entre_times(objeto1, objeto2):
    minutos_objeto1 = time_by_min(objeto1)
    minutos_objeto2 = time_by_min(objeto2)

    diferenca_minutos = minutos_objeto2 - minutos_objeto1

    if diferenca_minutos < 0:
        diferenca_minutos += 24 * 60  

    return diferenca_minutos


def seccionamento_by_lin(lin, list_datas, dados):
    dates_seccionament = []
    for dat in list_datas:
        if dat.weekday() in dados[lin]['FREQUÊNCIA']:
            dates_seccionament.append(dat)

    return dates_seccionament


def encontra_caracter(texto, caracter):
    aux_caracter = [x for x in range(len(texto)) if texto[x] == str(caracter).strip()]

    return(aux_caracter)


def trata_lin(linha, dados, list_datas):
    secc_by_lin = seccionamento_by_lin(linha, list_datas, dados)
    
    st.info(secc_by_lin)
    retorno = {}
    for dat_secc in secc_by_lin:

        for direc, value_aux in dados[linha]['PERCURSO'].items():
        
            print('-'*30+direc+'-'*30)
            new_dat_inic = datetime.strptime(f"{dat_secc} {[values['HORÁRIO CHEGADA'][-8:] for key, values in value_aux.items()][0]}", '%Y-%m-%d %H:%M:%S')
            
            
            cont = time_by_min(new_dat_inic.time())

            date_aux = new_dat_inic.date()
            last_date = new_dat_inic.time()

            
            for cod_secc, value in value_aux.items():
                
                print('-'*10+dados[linha]['PERCURSO'][direc][cod_secc]['SECCIONAMENTO']+'-'*10)

                aux_scc = str(dados[linha]['PERCURSO'][direc][cod_secc]['HORÁRIO CHEGADA']).strip()
                data_secc = datetime.strptime(str(aux_scc[min(encontra_caracter(aux_scc, ':'))-2:]).strip(), "%H:%M:%S").time()

                dif_min = diferenca_minutos_entre_times(last_date, data_secc)

                last_date = data_secc
                #SEPARANDO AS HORAS E MINUTOS DA DIFERENÇA
                cont += dif_min
                
                if cont >= 1440:
                    date_aux += timedelta(days=1)
                    cont -= 1440

                
                #SUBESCREVENDO AS DATAS E HORAS COM O FORMATO CORRETO
                retorno_hrs_chegada = f'{date_aux} {data_secc.hour}:{data_secc.minute}:00'
                
                dados[linha]['PERCURSO'][direc][cod_secc]['HORÁRIO CHEGADA'] = retorno_hrs_chegada

                #TRANTANDO O DADO DE TEMPO PARADO PARA SOMAR JUNTO A HORAS CHEGADA
                parada_time = datetime.strptime(dados[linha]['PERCURSO'][direc][cod_secc]['TEMPO DE PARADA'].strip()[-8:], '%H:%M:%S')
                parada_timedelta = timedelta(hours=parada_time.hour, minutes=parada_time.minute, seconds=parada_time.second)

                dados[linha]['PERCURSO'][direc][cod_secc]['HORÁRIO SAIDA'] = str(datetime.strptime(retorno_hrs_chegada, "%Y-%m-%d %H:%M:%S") + parada_timedelta)

                print(f'HORAS CHEGADA {retorno_hrs_chegada}')
                print(f'PARADA {parada_time}')
                print(f'HORA FINAL {datetime.strptime(retorno_hrs_chegada, "%Y-%m-%d %H:%M:%S") + parada_timedelta}')

        retorno[str(dat_secc)] = dados[linha]
    
    return retorno






#APRESENTAÇÃO DO FRONT
st.subheader('Frequência Semanal')

date_ini = st.date_input('Início', None)

retorno = None
if date_ini is not None:
    retorno = date_ini + timedelta(days=14)


date_fim = st.date_input('Fim', retorno)

list_datas = []
if None not in (date_ini, date_fim):
    
    while date_ini <= date_fim:
        list_datas.append(date_ini)
        date_ini += timedelta(days=1)


if len(list_datas) > 0:
    
    linhas_func = {}
    cont = 0
    #PUXANDO SOMENTE AS LINHAS QUE ATENDEM NAQUELE PERÍODO
    for lin in linhas_dados:
        
        secc_by_linha = linhas_dados[lin]['FREQUÊNCIA']

        merge_dates = [dat for dat in list_datas if dat.weekday() in secc_by_linha]
        if len(merge_dates) > 0: 
            cont+= 1
            linhas_func[lin] = linhas_dados[lin]

    linhaSelect = ''
    if len(linhas_func) > 0:
        linhaSelect = st.multiselect("Linhas", list(set([f'{lin} // {value["LINHA"]}' for lin, value in linhas_func.items()])), placeholder="Escolha as linhas que deseja visualizar")

    if len(linhaSelect) > 0:
        dados_select = {lin_select: linhas_func[str(str(lin_select).split('//')[0]).strip()] for lin_select in linhaSelect}

        dadosLinha = {}
        for lin in linhaSelect:

            st.success(f'{lin}')
            ddLin = trata_lin(lin, dados_select, list_datas)

            st.error(ddLin)
            #dadosLinha[lin] = ddLin
        
        #st.write(dadosLinha)
        #st.write(teste)
        #st.write(dados_select)

        


