"""Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário,
 utilizando a API ViaCEP.
 O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado."""
 
import requests
def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'erro' not in data:
            return {
                'logradouro': data['logradouro'],
                'bairro': data['bairro'],
                'cidade': data['localidade'],
                'estado': data['uf']
            }
        else:
            return None
    else:
        return None 

cep = input("Digite o CEP (somente números): ")
resultado = consultar_cep(cep)
if resultado:
    print("Informações do endereço:")
    print(f"Logradouro: {resultado['logradouro']}")
    print(f"Bairro: {resultado['bairro']}")
    print(f"Cidade: {resultado['cidade']}")
    print(f"Estado: {resultado['estado']}")
else:
    print("CEP inválido ou não encontrado.")      



