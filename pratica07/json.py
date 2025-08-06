"""
Crie um script em Python que leia e escreva dados em um arquivo JSON. 
O arquivo JSON deve conter informações de uma pessoa, com campos
 nome, idade e cidade.
"""
import json
def escrever_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, "w") as arquivo_json:
            json.dump(dados, arquivo_json, indent=4)
        print(f"Dados salvos com sucesso em {nome_arquivo}.")
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo_json:
            dados = json.load(arquivo_json)
            return dados
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

dados = {
    "nome": "Ana",
    "idade": 30,
    "cidade": "Rio de Janeiro"
}   
if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo JSON: ")
    escrever_json(nome_arquivo, dados)
    
    # Lendo os dados do arquivo JSON
    dados_lidos = ler_json(nome_arquivo)
    if dados_lidos:
        print(f"Dados lidos do arquivo {nome_arquivo}:")
        print(dados_lidos)