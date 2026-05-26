import csv

# Caminho para o arquivo CSV
arquivo_path: str = "exemplo.csv"

# Inicializa uma lista vazia para armazenar os dados
dados_csv: list = []

# Usa o gerenciador de contexto "with" para abrir o arquivo
with open(file=arquivo_path, mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)    # Cria um objeto leitor de CSV
    for linha in leitor_csv:                # Itera sobre as linhas do arquivo CSV
        dados_csv.append(linha)             # Adiciona cada linha (um dicionário) à lista de dados
for arquivo in dados_csv:                   # Exibe os dados lidos do arquivo CSV
    print(arquivo)
