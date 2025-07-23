'''
Calculadora de Desconto 

Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:
Nome do produto: "Camiseta"
Preço original: R$ 50.00
Porcentagem de desconto: 20% 
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhe
'''

# dados do enunciado
nome_produto = "camiseta"
preco_produto = 50.00
porcentagem_desconto = 20

# calculo descontos
valor_desconto = (preco_produto * porcentagem_desconto) / 100
preco_final = preco_produto - valor_desconto

# exibir resultados
print(f"produto: {nome_produto}")
print(f"preço original: R$ {preco_produto:.2f}")
print(f"porcentagem de desconto: {porcentagem_desconto}%")
print(f"valor de desconto: R$ {valor_desconto:.2f}")
print(f"preço final: R$ {preco_final:.2f}")