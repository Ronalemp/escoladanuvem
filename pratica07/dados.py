"""
Crie um script em Python que escreva dados em um arquivo CSV.
 O arquivo CSV deve conter informações pessoais,
  como colunas Nome, Idade e Cidade.
"""
import csv

# 1. Defina os dados que você quer escrever no CSV
#    A primeira lista será o cabeçalho das colunas.
#    As listas seguintes serão as linhas de dados.
cabecalho = ['Nome', 'Idade', 'Cidade']

dados = [
    ['Ana Souza', 28, 'Salvador'],
    ['João Silva', 35, 'São Paulo'],
    ['Maria Oliveira', 42, 'Rio de Janeiro'],
    ['Pedro Santos', 29, 'Belo Horizonte']
]

# 2. Defina o nome do arquivo CSV de saída
nome_arquivo = 'informacoes_pessoais.csv'

# 3. Abra o arquivo no modo de escrita ('w') com 'newline='
#    O 'newline=' é importante para evitar linhas em branco extras no arquivo.
with open(nome_arquivo, 'w', newline='') as arquivo_csv:
    # Crie um objeto 'writer' para escrever no arquivo
    writer = csv.writer(arquivo_csv)

    # 4. Escreva a linha do cabeçalho
    writer.writerow(cabecalho)

    # 5. Escreva as linhas de dados
    writer.writerows(dados)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")