"""Crie um programa que permita a um professor registrar as notas de uma turma.
  O programa deve continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando.
  No final, deve exibir a média da turma."""    

# Inicializa a lista para armazenar as notas
notas = []

print("Bem-vindo ao sistema de registro de notas.")
print("Digite as notas dos alunos. Digite 'fim' para terminar.")

# Loop para coletar as notas
while True:
    entrada = input("Digite a nota (0-10) ou 'fim' para encerrar: ")

    # Verifica se o usuário quer encerrar
    if entrada.lower() == 'fim':
        break

    try:
        # Converte a entrada para um número float
        nota = float(entrada)

        # Verifica se a nota é válida (entre 0 e 10)
        if 0 <= nota <= 10:
            notas.append(nota)
            print(f"Nota {nota} registrada com sucesso.")
        else:
            print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
    except ValueError:
        # Captura o erro se a entrada não for um número
        print("Entrada inválida. Por favor, digite um número ou 'fim'.")

# Calcula a média se houver notas na lista
if notas:
    media = sum(notas) / len(notas)
    print("\n--- Resultados ---")
    print(f"Número de notas registradas: {len(notas)}")
    print(f"A média da turma é: {media:.2f}")
else:
    print("\nNenhuma nota foi registrada.")

  


