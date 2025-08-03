
"""Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. 
O programa deve exibir o nome, email e país do usuário gerado."""
import requests
def gerar_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        user_info = data['results'][0]
        
        nome = f"{user_info['name']['first']} {user_info['name']['last']}"
        email = user_info['email']
        pais = user_info['location']['country']
        
        return {
            'nome': nome,
            'email': email,
            'pais': pais
        }
    else:
        return None

usuario = gerar_usuario_aleatorio()
if usuario:
    print("Usuário gerado com sucesso!")
    print(f"Nome: {usuario['nome']}")
    print(f"Email: {usuario['email']}")
    print(f"País: {usuario['pais']}")
else:
    print("Erro ao gerar usuário.")  
 