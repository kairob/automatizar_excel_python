import pandas as pd

# Substitua 'caminho/do/arquivo.xlsx' pelo caminho do seu arquivo Excel
arquivo_excel = 'caminho/do/arquivo.xlsx'

# Lê todas as planilhas do arquivo Excel
planilhas = pd.read_excel(arquivo_excel, sheet_name=None)

# Exemplo: imprime o nome das planilhas e as 5 primeiras linhas de cada uma
for nome, df in planilhas.items():
    print(f'Planilha: {nome}')
    print(df.head())
    print('-' * 40)