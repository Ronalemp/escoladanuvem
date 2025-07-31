"""2- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

Criança (0-12 anos),

Adolescente (13-17 anos),

Adulto (18-59 anos)

Idoso (60 anos ou mais)"""

if __name__ == "__main__":
    idade = int(input("Digite a sua idade: "))

    if 0 <= idade <= 12:
        print("Criança")
    elif 13 <= idade <= 17:
        print("Adolescente")
    elif 18 <= idade <= 59:
        print("Adulto")
    elif idade >= 60:
        print("Idoso")
    else:
        print("Idade inválida")  # Caso a idade seja negativa ou não seja um número inteiro

# Fim do código