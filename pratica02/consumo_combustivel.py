"""4- Calculadora de Consumo de Combustível

Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:
Distância percorrida: 300 km

Combustível gasto: 25 litros 
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

"""
# Dados da viagem
distancia_percorrida = 300 #float
combustivel_gasto = 25 #float

# Cálculo do consumo médio
consumo_medio = distancia_percorrida / combustivel_gasto

# Exibição dos resultados
print("Dados da Viagem")
print(f"Distância percorrida: {distancia_percorrida:.2f} km")
print(f"Combustível gasto: {combustivel_gasto:.2f} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")

