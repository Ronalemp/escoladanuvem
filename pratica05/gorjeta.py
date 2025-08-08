"""
Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros: valor_conta (float): O valor total da conta porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
Retorna: float: O valor da gorjeta calculada
"""
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
  """
  Calcula o valor da gorjeta a ser deixada em um restaurante.

  Args:
    valor_conta (float): O valor total da conta.
    porcentagem_gorjeta (float): A porcentagem da gorjeta desejada (ex: 15 para 15%).

  Returns:
    float: O valor da gorjeta calculada.
  """
  valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
  return valor_gorjeta

# Exemplo de uso:
valor_total_da_conta = input("Digite o valor total da conta: R$ ")
valor_total_da_conta = float(valor_total_da_conta)
if valor_total_da_conta < 0:
    raise ValueError("O valor da conta não pode ser negativo.")   
porcentagem_desejada = 15

gorjeta = calcular_gorjeta(valor_total_da_conta, porcentagem_desejada)

print(f"O valor total da conta é: R${valor_total_da_conta:.2f}")
print(f"A porcentagem de gorjeta desejada é: {porcentagem_desejada}%")
print(f"O valor da gorjeta a ser deixada é: R${gorjeta:.2f}")
print(f"O valor total a ser pago (conta + gorjeta) é: R${valor_total_da_conta + gorjeta:.2f}")
