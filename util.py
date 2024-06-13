import streamlit as st
from conexao import conexaoBD
from time import sleep

def cabecalho(nome):
    html = f"""<head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=M+PLUS+Rounded+1c:wght@700&display=swap" rel="stylesheet">
        </head>
        <body>
            <div class="fixed">
                <div class="menu">
                    <div class="logo">
                        <!-- <img src="https://raw.githubusercontent.com/RahyanRamos/Imagens.Eucatur/main/LogoProjeu_semFundo.png" alt="Logo projeu"> -->
                        <p>LOGO DO SIS.</p>
                    </div>
                    <div class="nome"><p>{nome}</p></div>
                    <!-- <div class="icone">
                        <button type="button"><img src="https://cdn-icons-png.flaticon.com/128/1570/1570102.png" alt="ícone de configurações para alteração do módulo de uso"></button>
                        <div class="modulo">
                            <a href="https://projetos.ngrok.pro"><button type="button">Módulo de Execução</button></a>
                        </div>
                    </div> -->
                </div>
            </div>
        </body>"""
    
    css = f""".fixed{{
            position: fixed;
            top: 0;
            z-index: 999990;
            left: 50px;
            right: 50px;
        }}

        .menu{{
            display: flex;
            position: absolute;
            align-items: center;
            background: #FFA3AF;
            color: #000;
            padding: 10px 20px;
            width: 100%;
            height: 60px;
            border-bottom-left-radius: 30px;
            border-bottom-right-radius: 30px;
        }}

        .logo{{
            margin-right: auto;
        }}

        .logo img,
        .logo h3{{
            min-width: 50px;
            max-width: 50px;
            min-height: 35px;
            max-height: 35px;
            font-family: 'M PLUS Rounded 1c', sans-serif;
            font-size: 40px;
            margin: 0;
        }}

        .nome p{{
            margin-right: 50px;
            color: #000;
            font-weight: bold;
            font-size: 16px;
            margin-top: 12px;
        }}

        .icone img{{
            width: 30px;
            height: 30px;
        }}

        .icone button{{
            background-color: #9dacbb;
            border-radius: 50%;
            cursor: pointer;
            border: none;
            width: 40px;
            height: 40px;
        }}

        .modulo{{
            display: none;
            position: absolute;
            top: auto;
            right: 0;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            background-color: #e6dde6;
            height: auto;
            width: 175px;
            border-radius: 10px;
            padding: 10px;
            margin-top: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
        }}

        .modulo button{{
            border-radius: 8px;
        }}

        .modulo:after{{
            content: "";
            width: 0;
            height: 0;
            position: absolute;
            border-left: 15px solid transparent;
            border-right: 15px solid transparent;
            border-bottom: 20px solid #e6dde6;
            top: -15px;
            right: 25px
        }}

        .icone:hover .modulo{{
            display: block;
        }}

        .modulo button{{
            display: block;
            width: 100%;
            padding: 5px;
            text-align: left;
            background-color: transparent;
            border: none;
            cursor: pointer;
            font-weight: bold;
            color: #000;
            margin-bottom: 5px;
        }}

        .modulo button:hover{{
            background-color: #dac0da;
        }}

        .logo:hover{{
            text-decoration: underline;
        }}
        
        @media only screen and (max-width: 600px) {{
            .menu {{
                padding: 10px;
            }}

            .logo img,
            .logo h3 {{
                font-size: 24px;
            }}

            .nome p {{
                margin-right: 20px;
                font-size: 12px;
            }}

            .icone img {{
                width: 24px;
                height: 24px;
            }}

            .icone button {{
                width: 25px;
                height: 25px;
            }}

            .modulo {{
                width: 180px;
            }}

            .modulo button{{
                width: 100%;
                margin: 0px 0px 10px;
            }}
        }}"""

    st.write(html, unsafe_allow_html=True)
    st.write(f"<style>{css}</style>", unsafe_allow_html=True)

def cabEscala():
    html = """<div class="cabecalho">
            <div class="titulo">
                <p>Gestão de Escalas</p>
            </div>
        </div>"""
    
    css = """@import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap');

        p{
            font-family: "Open Sans", sans-serif;
        }
    
        .cabecalho {
            margin: 0;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 59px;
            display: flex;
            justify-content: center;
            align-items: center;
            background-position: center;
            z-index: 999990;
            background-color: #f0f0f0;
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.3);
        }

        .cabecalho .titulo {
            position: relative;
            z-index: 2;
            color: #000;
            text-align: center;
            background-color: #9dacbb;
            padding: 0 5px;
            border-radius: 16px;
        }

        .cabecalho .titulo p{
            margin: 3px;
            font-family: "Open Sans", sans-serif;
            font-size: 24px;
            font-weight: bold;
        }

        [data-testid="collapsedControl"]{
           z-index: 999991;
           background-color: #9dacbb;
           height: 59px;
           width: 100px;
           left: 0;
           top: 0;
           padding: 5px;
        }
        
        [data-testid="collapsedControl"] img{
            width: 35px;
            height: 35px;
        }

        [data-testid="stSidebar"][aria-expanded="true"] img{
            width: 120px;
            height: 35px;
        }
        
        [data-testid="collapsedControl"] svg,
        [data-testid="stSidebar"][aria-expanded="true"] svg{
            height: 30px;
            width: 30px;
            margin: 5px 0;
        }"""
    st.write(f"<div>{html}</div>", unsafe_allow_html=True)
    st.write(f"<style>{css}</style>", unsafe_allow_html=True)
    st.logo("https://raw.githubusercontent.com/RahyanRamos/Imagens.Eucatur/main/logo-EscalaMax.png", link="http://localhost:8501/", icon_image="https://raw.githubusercontent.com/RahyanRamos/Imagens.Eucatur/main/logoIcon-EscalaMax.png")


# .st-ae{
#     background-color: blue;
# }

def botaoHome(nome, img, link):
    html = f"""<div class="botaoHome">
            <a href="{link}" target="_self">
                <img src="{img}" alt="Ícone para o botão de {nome}">
                <button type="button">
                    {nome}
                </button>
            </a>
        </div>"""
    
    css = """.botaoHome {
            margin: 10px;
            text-align: center;
            background-color: #9dacbb;
            padding: 8px;
            width: 100%;
            border-radius: 24px;
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.1);
        }

        .botaoHome a {
            text-decoration: none;
            color: inherit;
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
        }

        .botaoHome img {
            width: 42px;
            height: 42px;
        }

        .botaoHome button {
            background-color: transparent;
            color: #000;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: underline;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            font-weight: bold;
            font-family: "Open Sans", sans-serif;
        }

        .botaoHome:hover{
            background-color: #819fbd;
            transform: scale(1.05);
            box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
            cursor: pointer;
        }"""
    
    st.write(f"<div>{html}</div>", unsafe_allow_html=True)
    st.write(f"<style>{css}</style>", unsafe_allow_html=True)

def tituloPage(titulo):
    html = f"""<div class="header">
            <hr>
            <p>{titulo.upper()}</p>
            <hr>
        </div>"""

    css = """@import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap');
    
        .header{
            width: 99%;
            margin: 0 auto;
            display: flex;
            align-items: center;
        }

        .header hr{
            flex: 1;
            border: none;
            border-top: 3px solid #333;
            border-radius: 8px;
            margin: 0;
        }

        .header p{
            font-size: 2em;
            font-weight: bold;
            font-family: font-family: "Open Sans", sans-serif;
            width: max-content;
            margin: 0 auto;
            text-align: center;
            white-space: nowrap;
            color: #000;
            padding: 0 5px;
        }"""
    
    st.write(f"<div>{html}</div>", unsafe_allow_html=True)
    st.write(f"<style>{css}</style>", unsafe_allow_html=True)

def tabelas(page, dados):
    if page == "Motorista":
        html = """<div class="tabela">
                <table>
                    <tr>
                        <th>Matrícula</th>
                        <th>Nome</th>
                        <th>Unidade</th>
                        <th>Cidade de Origem</th>
                        <th>Função</th>
                        <th>Situação</th>
                        <th>Ações</th>
                    </tr>"""
        
        for ddMotorista in dados:
            if ddMotorista[11]:
                situacao = "Escalado"
            elif ddMotorista[12]:
                situacao = ""
                for sit in ddMotorista[12].split("~/>"):
                    situacao += f"{sit}; "
            else:
                situacao = " "

            html += f"""<tr>
                    <td>{ddMotorista[7]}</td>
                    <td>{ddMotorista[1]}</td>
                    <td>{ddMotorista[8]}</td>
                    <td>{ddMotorista[9]}</td>
                    <td>{ddMotorista[10]}</td>
                    <td>{situacao}</td>
                    <td class="acao">
                        <a href="http://localhost:8501/novoMotorista/?funcao=editar&id={ddMotorista[0]}" target="_self">
                            <img src="https://cdn-icons-png.flaticon.com/128/1159/1159633.png" alt="Ícone de editar dado" title="Editar Motorista">
                        </a>
                        <a href="http://localhost:8501/novoMotorista/?funcao=ausencia&id={ddMotorista[0]}" target="_self">
                            <img src="https://cdn-icons-png.flaticon.com/128/4753/4753030.png" alt="Ícone de registrar ausência" title="Registrar Ausência">
                        </a>
                        <a href="http://localhost:8501/Motoristas/?funcao=excluir&id={ddMotorista[0]}" target="_self">
                            <img src="https://cdn-icons-png.flaticon.com/128/4347/4347443.png" alt="Ícone de excluir dado" title="Excluir Motorista">
                        </a>
                    </td>
                </tr>"""

    css = """.tabela{
            max-height: 500px;
            overflow-y: auto;
            overflow-x: hidden;
            border-radius: 16px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            font-family: "Open Sans", sans-serif;
            font-size: 14px;
        }

        .tabela::-webkit-scrollbar{
            width: 5px;
        }

        .tabela::-webkit-scrollbar-track{
            background-color: #dfefff;
            border-radius: 10px;
        }

        .tabela::-webkit-scrollbar-thumb{
            background-color: #9dacbb;
            border-radius: 10px;
        }

        .tabela::-webkit-scrollbar-thumb:hover{
            background-color: #819fbd;
        }

        .tabela table{
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            margin: 0;
            background-color: #bfd6ec;
            border: 1px solid #788da1;
            border-radius: 16px;
            color: #000;
        }

        .tabela th{
            background-color: #456c91;
            color: #ebf6ff;
            position: sticky;
            top: 0;
        }

        .tabela tr th{
            padding: 5px;
            text-align: center;
            font-weight: bold;
        }

        .tabela tr:nth-child(even){
            background-color: #a6c7e5;
        }

        .tabela tr:hover{
            background-color: #91a9c0;
        }

        .tabela tr td{
            padding: 5px;
            border: None;
            text-align: center;
        }

        .tabela tr td img{
            width: 20px;
            height: 20px;
            cursor: pointer;
            transition: transform 0.3s;
            text-align: center;
            margin: 0 3px;
        }

        .tabela .acao{
            display: flex;
            justify-content: center;
            gap: 10px;
            align-items: center;
        }

        .tabela tr td img:hover{
            transform: scale(1.2);
        }

        .tabela tr:first-child th:first-child{
            border-top-left-radius: 10px;
        }

        .tabela tr:first-child th:last-child{
            border-top-right-radius: 10px;
        }

        .tabela tr:last-child td:first-child{
            border-bottom-left-radius: 10px;
        }

        .tabela tr:last-child td:last-child{
            border-bottom-right-radius: 10px;
        }"""

    st.write(f"<div>{html}</div>", unsafe_allow_html=True)
    st.write(f"<style>{css}</style>", unsafe_allow_html=True)

@st.experimental_dialog("EXCLUIR MOTORISTA")
def excluirMotorista(id, nome, matricula):
    st.text(f"Matrícula: {matricula}")
    st.text(f"Nome: {nome}")
    st.write("O motorista ficará inativo no sistema")

    colAux, colNao, colSim = st.columns([2, 1, 1])

    with colNao:
        cancelar = st.button("Cancelar", use_container_width=True)
    with colSim:
        aceitar = st.button("Aceitar", use_container_width=True)

    if aceitar:
        conexao = conexaoBD()
        mycursor = conexao.cursor()

        sql = f"UPDATE motoristas_lista SET status_motorista = 0 WHERE id_mot = {id}"
        mycursor.execute(sql)
        conexao.commit()

        mycursor.close()
        conexao.close()

        st.query_params.clear()
        st.toast(f"Motorista {nome} inativado com sucesso!", icon="✅")
        sleep(1)
        st.rerun()
    elif cancelar:
        st.query_params.clear()
        st.rerun()

def sideBar():
    st.sidebar.page_link("Home.py")
    st.sidebar.page_link("pages/1 - Linhas.py")
    st.sidebar.page_link("pages/2 - Motoristas.py")
    st.sidebar.page_link("pages/3 - Escalas.py")
    st.sidebar.page_link("pages/99 - Configurações.py")