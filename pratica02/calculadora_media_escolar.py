"""
calculadora media escolar

Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:
Nota 1: 7.5
Nota 2: 8.0
Nota 3: 6.5 
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
"""
# Notas do aluno
nota1 = 7.5 #float
nota2 = 8.0 #float
nota3 = 6.5 #float

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# exibiçao de resultados
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Nota 3: {nota3:.2f}")
print(f"Média: {media:.2f}")