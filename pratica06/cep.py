"""Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário,
 utilizando a API ViaCEP. 
O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado."""

import requests

def consultar_cep(cep):
    """
    Consulta informações de endereço a partir de um CEP utilizando a API ViaCEP.

    Args:
        cep (str): O CEP a ser consultado.

    Returns:
        dict: Um dicionário contendo as informações de endereço ou uma mensagem de erro.
    """
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"erro": "CEP não encontrado"}

# Exemplo de uso:
cep = input("Digite o CEP: ")
dados_endereco = consultar_cep(cep)
if "erro" not in dados_endereco:
    print("Endereço encontrado:")
    print(f"Logradouro: {dados_endereco['logradouro']}")
    print(f"Bairro: {dados_endereco['bairro']}")
    print(f"Cidade: {dados_endereco['localidade']}")
    print(f"Estado: {dados_endereco['uf']}")
else:
    print(dados_endereco["erro"]) 

    