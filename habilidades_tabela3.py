import pandas as pd

# Nome dos arquivos CSV (adapte para os seus arquivos)
arquivo_habilidades = "habilidades.csv"
arquivo_relacionamentos = "relacionamentos.csv"


def gerar_tabela(arquivo_habilidades, arquivo_relacionamentos):
    """
    Gera uma tabela HTML exibindo o relacionamento entre habilidades e informações.

    Args:
        arquivo_habilidades: Caminho para o arquivo CSV com os códigos de habilidades.
        arquivo_relacionamentos: Caminho para o arquivo CSV com os relacionamentos.
    """

    try:
        df_habilidades = pd.read_csv(arquivo_habilidades)
        df_relacionamentos = pd.read_csv(arquivo_relacionamentos)
    except FileNotFoundError:
        print(f"Erro: Arquivo(s) CSV não encontrado(s).")
        return

    # Certifica-se de que 'codigo_habilidade' e 'informacao' existam nos DataFrames
    if not all(col in df_relacionamentos.columns for col in ['codigo_habilidade', 'componente', 'informacao']):
        print("Erro: Colunas 'codigo_habilidade', 'componente' ou 'informacao' não encontradas no arquivo de relacionamentos.")
        return

     # Cria um dicionário para armazenar as informações relacionadas a cada habilidade
    habilidades_info = {}
    for _, row in df_relacionamentos.iterrows():
        codigo = row['codigo_habilidade']
        comp = row['componente']
        info = row['informacao']
        desc = row['descricao']
        cod_comp = row['comp_cod']
        if codigo not in habilidades_info:
            habilidades_info[codigo] = []
        habilidades_info[codigo].append(cod_comp)

    # Dicionário de cores por código de habilidade completo
    pensComp = "#ADD8E6" # Azul claro - PENSAMENTO COMPUTACIONAL
    munDig   = "#90EE90"  # Verde claro - MUNDO DIGITAL
    cultDig  = "#FFFFE0"  # Amarelo claro - CULTURA DIGITAL

    
    cores_habilidades = {
        "(EF01CO01)": pensComp,
        "(EF01CO02)": pensComp,
        "(EF01CO03)": pensComp,
        "(EF01CO04)": munDig,
        "(EF01CO05)": munDig,
        "(EF01CO06)": cultDig,
        "(EF01CO07)": cultDig,
        "(EF02CO01)": pensComp,
        "(EF02CO02)": pensComp,
        "(EF02CO03)": munDig,
        "(EF02CO04)": munDig,
        "(EF02CO05)": cultDig,
        "(EF02CO06)": cultDig,
        "(EF03CO01)": pensComp,
        "(EF03CO02)": pensComp,
        "(EF03CO03)": pensComp,
        "(EF03CO04)": munDig,
        "(EF03CO05)": munDig,
        "(EF03CO06)": munDig,
        "(EF03CO07)": cultDig,
        "(EF03CO08)": cultDig,
        "(EF03CO09)": cultDig,
        "(EF04CO01)": pensComp,
        "(EF04CO02)": pensComp,
        "(EF04CO03)": pensComp,
        "(EF04CO04)": munDig,
        "(EF04CO05)": munDig,
        "(EF04CO06)": cultDig,
        "(EF04CO07)": cultDig,
        "(EF04CO08)": cultDig,
        "(EF05CO01)": pensComp,
        "(EF05CO02)": pensComp,
        "(EF05CO03)": pensComp,
        "(EF05CO04)": pensComp,
        "(EF05CO05)": munDig,
        "(EF05CO06)": munDig,
        "(EF05CO07)": munDig,
        "(EF05CO08)": cultDig,
        "(EF05CO09)": cultDig,
        "(EF05CO10)": cultDig,
        "(EF05CO011)": cultDig,
        "(EF15CO01)": pensComp,
        "(EF15CO02)": pensComp,
        "(EF15CO03)": pensComp,
        "(EF15CO04)": pensComp,
        "(EF15CO05)": munDig,
        "(EF15CO06)": munDig,
        "(EF15CO07)": munDig,
        "(EF15CO08)": cultDig,
        "(EF15CO09)": cultDig,
        "(EF06CO01)": pensComp,
        "(EF06CO02)": pensComp,
        "(EF06CO03)": pensComp,
        "(EF06CO04)": pensComp,
        "(EF06CO05)": pensComp,
        "(EF06CO06)": pensComp,
        "(EF06CO07)": munDig,
        "(EF06CO08)": munDig,
        "(EF06CO09)": cultDig,
        "(EF06CO10)": cultDig,
        "(EF07CO01)": pensComp,
        "(EF07CO02)": pensComp,
        "(EF07CO03)": pensComp,
        "(EF07CO04)": pensComp,
        "(EF07CO05)": pensComp,
        "(EF07CO06)": munDig,
        "(EF07CO07)": munDig,
        "(EF07CO08)": cultDig,
        "(EF07CO09)": cultDig,
        "(EF07CO10)": cultDig,
        "(EF07CO11)": cultDig,
        "(EF08CO01)": pensComp,
        "(EF08CO02)": pensComp,
        "(EF08CO03)": pensComp,
        "(EF08CO04)": pensComp,
        "(EF08CO05)": munDig,
        "(EF08CO06)": munDig,
        "(EF08CO07)": cultDig,
        "(EF08CO08)": cultDig,
        "(EF08CO09)": cultDig,
        "(EF08CO10)": cultDig,
        "(EF08CO11)": cultDig,
        "(EF09CO01)": pensComp,
        "(EF09CO02)": pensComp,
        "(EF09CO03)": pensComp,
        "(EF09CO04)": munDig,
        "(EF09CO05)": munDig,
        "(EF09CO06)": cultDig,
        "(EF09CO07)": cultDig,
        "(EF09CO08)": cultDig,
        "(EF09CO09)": cultDig,
        "(EF09CO10)": cultDig,
        "(EF69CO01)": pensComp,
        "(EF69CO02)": pensComp,
        "(EF69CO03)": pensComp,
        "(EF69CO04)": pensComp,
        "(EF69CO05)": pensComp,
        "(EF69CO06)": pensComp,
        "(EF69CO07)": munDig,
        "(EF69CO08)": munDig,
        "(EF69CO09)": munDig,
        "(EF69CO10)": munDig,
        "(EF69CO11)": cultDig,
        "(EF69CO12)": cultDig,
    }

    # Dicionário para mapear componentes por cores nos dados das habilidades relacionadas
    cores_componentes = {
        "Ciências": "#481EFF",  # Azul medio
        "Geografia": "#8A2BE2",  # Verde claro
        "História": "#FFB6C1",  # Rosa claro
        "Matemática": "#E3E353",  # Amarelo claro
        "Língua Portuguesa": "#87CEFA",  # Azul céu
        "Arte": "#DA70D6", # Orquídea
        "Língua Inglesa": "#DDA0DD", # Ametista
        "Outro": "#708090", # Cinza ardósia
        "Educaçao Física": "#CCCCCC" #Cinza
        # Adicione mais componentes e cores conforme necessário
    }

    cor_padrao = "#FFFFFF"  # Branco

    # Gera a tabela HTML
    tabela_html = "<table>\n<thead><tr>"

    # Cria um dicionário para armazenar as informações relacionadas a cada habilidade e exibe na tabela
    for _, row in df_habilidades.iterrows():
        codigo = row['codigo']
        descricao = row['descricao']
        cor = cores_habilidades.get(codigo, cor_padrao) # Busca a cor pelo código completo
        tabela_html += f"<th style='background-color: {cor};'>{codigo}</th>"
    tabela_html += "</tr></thead>\n<tbody>"

    # Encontra o número máximo de linhas necessárias
    max_linhas = max(len(habilidades_info.get(codigo, [])) for codigo in df_habilidades['codigo'])

    for i in range(max_linhas):
        tabela_html += "<tr>"
        for codigo in df_habilidades['codigo']:
            if codigo in habilidades_info and i < len(habilidades_info[codigo]):
                informacao = habilidades_info[codigo][i]
                componente = df_relacionamentos[df_relacionamentos['codigo_habilidade'] == codigo]['componente'].iloc[i] if i < len(df_relacionamentos[df_relacionamentos['codigo_habilidade'] == codigo]) else None # lógica adicionada
                cor = cores_componentes.get(componente, cor_padrao) if componente else cor_padrao # Usa cores_componentes
                tabela_html += f"<td style='background-color: {cor};'>{informacao}</td>"
            else:
                tabela_html += f"<td style='background-color: {cor_padrao};'></td>" #célula vazia
        tabela_html += "</tr>\n"

    tabela_html += "</tbody></table>"

    tabela_html += "<p>Legendas das cores das habilidades da computação: </p>"
    tabela_html += f"<p style='background-color: {pensComp};'>Azul claro - PENSAMENTO COMPUTACIONAL</p>"
    tabela_html += f"<p style='background-color: {munDig};'>Verde claro - MUNDO DIGITAL</p>"
    tabela_html += f"<p style='background-color: {cultDig};'>Amarelo claro - CULTURA DIGITAL</p>"
    

    # Exibe a tabela (pode ser salvo em um arquivo HTML também)
    #print(tabela_html)

    # Grava a tabela gerada em um arquivo de texto
    with open("apoio.txt", "w") as f:  # Abre o arquivo para escrita
        f.write(tabela_html)

    print("Tabela HTML salva no arquivo")


# Executa a função
gerar_tabela(arquivo_habilidades, arquivo_relacionamentos)