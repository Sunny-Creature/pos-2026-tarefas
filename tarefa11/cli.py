import users_wrapper as u_wrapper

# listar usuários
print(u_wrapper.list_users())

# detalhar usuário
print(u_wrapper.detail_user(6))

# criar usuário
user_data = {
        'name': "Richard",
        'username': "Richard",
        'email': "richard@gmail.com",
        'address': "Lagoa Nova - Natal/RN",
        'phone': "99999-0000",
        'website': "www.richardempresas.com",
        'company': "Richard Empresas"
    }
print(u_wrapper.create_user(user_data))

# atualizar usuário
user_data = {
    'name': "James"
}
print(u_wrapper.update_user(8, user_data))

# deletar usuário
print(u_wrapper.delete_user(4))

opcao = input("Digite '1' para listar os usuários\n Digite '2' para detalhar um usuário\n Digite '3' para editar um usuário\n Digite '4' para remover um novo usuário\n Digite '5' para criar um novo usuário\n Digite qualquer coisa para sair")

if opcao == "1":
    print("Listagem de usuários")
    users = u_wrapper.list_users()
    for user in users[:10]:
        print(f"{user['id']} - {user['name']}")


elif opcao == "2":
    user_id = int(input("Digite o ID do usuário desejado para mais informações: "))

    user = u_wrapper.detail_user(user_id)
    print(f"Nome: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"Website: {user['website']}")

# elif opcao == "3":
#     user_id = input("Digite o ID do usuário desejado: ")
#     response = requests.patch(f"{api_url}/users/{user_id}")
#     if response.status_code == 200:
#         user = response.json()
#         print(f"Nome: {user["name"]}")

# elif opcao == "4":
#     user_id = input("Digite o ID do usuário que deseja remover: ")
#     response = requests.get(api_url+"/users/"+user_id)
#     if response.status_code == 200:
        

        
#     confirmar = input("Digite 'S' para confirmar a remoção do usuário: ")
#     if confirmar == 'S':
#         response = requests.delete(f"{api_url}/users/{user_id}/")
#         if response.status_code != 204:
#             print("Deu erro!")

# elif opcao == "5":
#     print(input("Digite os dados desejados para o novo usuário: "))
#     user = {}
#     user["name"] = input("Nome: ")
#     user["username"] = input("Usuário: ")
#     user["email"] = input("E-mail: ")
#     user["address"] = input("Endereço: ")
#     user["Phone"] = input("Telefone: ")
#     user["Website"] = input("Site: ")
#     user["Company"] = input("Empresa: ")

#     criar = (input("Digite 'S' para criar o novo usuário: "))
#     if criar == 'S':
#         response = requests.post