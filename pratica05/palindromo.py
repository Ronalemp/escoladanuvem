"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo 
(lê-se igual de trás para frente, ignorando espaços e pontuação). 
Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”
"""


def eh_palindromo(texto):
    """
    Verifica se uma palavra ou frase é um palíndromo.

    Args:
        texto (str): A palavra ou frase a ser verificada.

    Returns:
        bool: True se for um palíndromo, False caso contrário.
    """
    # Remove espaços e converte para minúsculas
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    # Verifica se o texto é igual ao seu reverso
    return texto_limpo == texto_limpo[::-1]

# Exemplo de uso:
texto = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
if eh_palindromo(texto):
    print(f"'{texto}' é um palíndromo? Sim")
else:
    print(f"'{texto}' é um palíndromo? Não")



