"""
Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning. 
Calcule a média e o desvio padrão do tempo de exercução constantes.
"""
import pandas as pd

# 1. Criar um DataFrame de exemplo
dados = {'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
         'Idade': [25, 30, 35, 40],
         'Salario': [50000, 60000, 75000, 90000]}

df = pd.DataFrame(dados)

# 2. Exibir o DataFrame
print("DataFrame Original:")
print(df)

# 3. Calcular a média da coluna 'Salario'
media_salario = df['Salario'].mean()

# 4. Imprimir o resultado
print(f"\nDataFrame Original:\n{df}")
print(f"\nMédia da coluna 'Salario': {media_salario:.2f}")