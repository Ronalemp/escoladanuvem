"""Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço final após a aplicação do desconto.
 Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10)."""

def calcular_preco_final(preco_original, percentual_desconto):
    """
    Calcula o preço final de um produto após a aplicação de um desconto.

    Args:
        preco_original (float): O preço original do produto.
        percentual_desconto (float): O percentual de desconto a ser aplicado.

    Returns:
        float: O preço final do produto após o desconto.
    """
    desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - desconto
    return preco_final

# Exemplo de uso:
preco = float(input("Digite o preço original do produto: R$ "))
percentual = float(input("Digite o percentual de desconto: "))
preco_final = calcular_preco_final(preco, percentual)
print(f"O preço final do produto após o desconto é: R$ {preco_final:.2f}")
