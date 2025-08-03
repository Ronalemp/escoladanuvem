"""Crie um programa que solicite ao usuário que insira números inteiros.
 O programa deve continuar solicitando números até que o usuário digite 'fim'.
  Para cada número inserido, o programa deve informar se é par ou ímpar. Se o usuário inserir algo que não seja um número inteiro,
  o programa deve informar o erro e continuar. No final, o programa deve exibir a quantidade de números pares e ímpares inseridos."""

  # Inicializa os contadores para números pares e ímpares
pares = 0
impares = 0

print("Bem-vindo ao verificador de paridade!")
print("Digite números inteiros. Digite 'fim' para encerrar.")

# Loop principal para solicitar os números
while True:
    entrada = input("Digite um número inteiro ou 'fim': ")

    # Verifica se o usuário quer sair
    if entrada.lower() == 'fim':
        break

    try:
        # Tenta converter a entrada para um número inteiro
        numero = int(entrada)

        # Verifica se o número é par ou ímpar
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
            pares += 1
        else:
            print(f"O número {numero} é ímpar.")
            impares += 1

    except ValueError:
        # Se a conversão falhar, exibe uma mensagem de erro
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

# Exibe o resultado final
print("\n--- Resumo ---")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")