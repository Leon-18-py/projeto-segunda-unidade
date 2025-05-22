import os

usuarios = list()

print("*"*50)
print("Bem vindo!")
print("*"*50)
while(True):
    opcao = input("Escolha uma das opções\n\n" \
     "1 - Cadastrar usuário\n"\
     "2 - Listar usuários\n"\
     "3 - Buscar usuário por email\n"\
     "4 - Remover usuáro por email\n"\
     "5 - Atualizar usuário por email\n"\
     "0 - Sair\n\n Opção: ")
    if(opcao == '0'):
        break
    elif(opcao == '1'):
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        while(not "@" in email or not email.endswith('.com')):
            print("Email inválido")
            email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        usuario = {
            "nome": nome,
            "email": email,
            "senha": senha
        }     
        emailRepetido = email
        encontrado = False
        for usu in usuarios:
            while(email == usu["email"]):
                encontrado = True
                print("Email já existente. Tente outro: ")
                email = input("Digite seu email: ")
                usuario = {"nome": nome,
                 "email": email,
                 "senha": senha
                    }    
        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")
        os.system('cls' if os.name == 'nt' else 'clear')

    elif(opcao == '2'):
        print("\nLista de usuários\n")
        for usu in usuarios:
            print(f"Nome: {usu["nome"]}")
            print(f"Email: {usu["email"]}")
            print("-"*50)
        print("\n")
    elif(opcao == '3'):
        emailBusca = input("Digite um email para busca: ")
        encontrado = False
        for usu in usuarios:
            if(emailBusca == usu["email"]):
                encontrado = True
                print("Encontrou o usuário\n\n")
                print("-"*50)
                print(f"Nome: {usu["nome"]}")
                print(f"Email: {usu["email"]}")
                print("-"*50)
        if(not encontrado):
            print("Usuário não existe!\n\n")
    elif(opcao == '4'):
        emailBusca = input("Digite um email para remover: ")
        indice = -1
        for ind in range(len(usuarios)):
            if(emailBusca == usuarios[ind]["email"]):
                indice = ind
        
        if(indice == -1):
            print("Não encontrado")
        else:
            usuarios.pop(indice)
    elif(opcao == '5'):
        emailBusca = input("Digite um email para atualizar: ")
        indice = -1
        for ind in range(len(usuarios)):
            if(emailBusca == usuarios[ind]["email"]):
                indice = ind
        
        if(indice == -1):
            print("Não encontrado")
        else:
            nomenovo = input("Digite seu novo nome: ")
            senhanova = input("Digite sua nova senha: ")

            usuarios[indice]["nome"] = nomenovo
            usuarios[indice]["senha"] = senhanova
    else:
        print("Opção inválida")