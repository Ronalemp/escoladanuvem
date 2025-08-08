"""Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). 
O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, 
máximo e mínimo da cotação, além da data e hora da última atualização. 
Utilize a API da AwesomeAPI para obter os dados de cotação."""
import requests
def consultar_cotacao(moeda):
    """
    Consulta a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL).

    Args:
        moeda (str): O código da moeda a ser consultada (ex: USD, EUR, GBP).

    Returns:
        dict: Um dicionário contendo as informações de cotação ou uma mensagem de erro.
    """
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"erro": "Moeda não encontrada"}   

# Exemplo de uso:
moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ")
dados_cotacao = consultar_cotacao(moeda)
if "erro" not in dados_cotacao:
    cotacao = dados_cotacao[f"{moeda}BRL"]
    print("Cotação encontrada:")
    print(f"Valor atual: R$ {cotacao['bid']}")
    print(f"Valor máximo: R$ {cotacao['high']}")
    print(f"Valor mínimo: R$ {cotacao['low']}")
    print(f"Data e hora da última atualização: {cotacao['create_date']}")
else:
    print(dados_cotacao["erro"])



