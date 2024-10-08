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

    # Verifica se as colunas necessárias existem
    if not all(col in df_relacionamentos.columns for col in ['codigo_habilidade', 'informacao']):
        print("Erro: Colunas 'codigo_habilidade' ou 'informacao' não encontradas no arquivo de relacionamentos.")
        return

    if not all(col in df_habilidades.columns for col in ['codigo', 'descricao']):
        print("Erro: Colunas 'codigo' ou 'descricao' não encontradas no arquivo de habilidades.")
        return

     # Cria um dicionário para armazenar as informações relacionadas a cada habilidade
    habilidades_info = {}
    for _, row in df_relacionamentos.iterrows():
        codigo = row['codigo_habilidade']
        info = row['informacao']
        if codigo not in habilidades_info:
            habilidades_info[codigo] = []
        habilidades_info[codigo].append(info)

    # Gera a tabela HTML
    tabela_html = "<table>\n<thead><tr>"
    for _, row in df_habilidades.iterrows():
        codigo = row['codigo']
        descricao = row['descricao']
        tabela_html += f"<th>{codigo} - {descricao}</th>"  # Inclui a descrição no cabeçalho
    tabela_html += "</tr></thead>\n<tbody>"

    # Encontra o número máximo de linhas necessárias
    max_linhas = max(len(habilidades_info.get(codigo, [])) for codigo in df_habilidades['codigo'])


    for i in range(max_linhas):
        tabela_html += "<tr>"
        for codigo in df_habilidades['codigo']:
            if codigo in habilidades_info and i < len(habilidades_info[codigo]):
                tabela_html += f"<td>{habilidades_info[codigo][i]}</td>"
            else:
                tabela_html += "<td></td>"  # Célula vazia se não houver informação
        tabela_html += "</tr>\n"




    tabela_html += "</tbody></table>"

    # Exibe a tabela (pode ser salvo em um arquivo HTML também)
    print(tabela_html)


# Executa a função
gerar_tabela(arquivo_habilidades, arquivo_relacionamentos)
