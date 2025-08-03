"""Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida 
seja inserida ou o usuário digite 'sair'."""

def verificar_senha_forte(senha):
    """
    Verifica se uma senha é forte com base em dois critérios:
    1. Ter pelo menos 8 caracteres.
    2. Conter pelo menos um número.
    """
    if len(senha) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres."

    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
            break
    
    if not tem_numero:
        return False, "A senha deve conter pelo menos um número."

    return True, "Senha forte e válida!"

# Loop principal do programa
while True:
    senha_digitada = input("Digite uma senha (ou 'sair' para sair): ")

    if senha_digitada.lower() == 'sair':
        print("Programa encerrado.")
        break

    eh_forte, mensagem = verificar_senha_forte(senha_digitada)

    if eh_forte:
        print(mensagem)
        break  # Sai do loop após uma senha forte ser inserida
    else:
        print(f"Senha inválida: {mensagem}")