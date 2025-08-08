"""Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, 
possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória."""

import random
def gerar_senha_aleatoria(tamanho=12):
    """
    Gera uma senha aleatória com o tamanho especificado, utilizando letras maiúsculas, minúsculas, números e caracteres especiais.

    Args:
        tamanho (int): O tamanho da senha a ser gerada. Padrão é 12.

    Returns:
        str: A senha aleatória gerada.
    """
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Exemplo de uso:
tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
if tamanho_senha <= 0:
    raise ValueError("O tamanho da senha deve ser um número positivo.")
senha_gerada = gerar_senha_aleatoria(tamanho_senha)
print(f"A senha aleatória gerada é: {senha_gerada}")
print("Lembre-se de guardar sua senha em um local seguro!") 