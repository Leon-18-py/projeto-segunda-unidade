import os

usuarios = list()
caronas = list()

print("*"*50)
print("Bem vindo!")
print("*"*50)
while(True):
    opcao = input("Escolha uma das opções\n\n" \
     "1 - Cadastrar usuário\n"\
     "2 - Login\n"\
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
        email = str(input("Digite o seu email: "))
        senha = input("Digite a sua senha: ")
        for ind in range(len(usuarios)):
            if(email == usuarios[ind]['email'] and senha == usuarios[ind]['senha']):
                print("Login efetivado")
                loggado = -1
                while(loggado != 0):
                    print("Menu Login\n")
                    print("Cadastro de carona")
                    print("Listar caronas")
                    print("Buscar carona por origem e destino")
                    print("Voltar menu inicial\n")
                    print("Escolha a opcao\n")
                    op=input("Informe a opcao: ")
                    if(op == '1'):
                        print("Cadastrando carona")
                        nomeMotorista = str(input("Digite seu nome: "))
                        localOrigem = str(input("Informe o local de origem: "))
                        destino = str(input("Informe o destino da carona: "))
                        data = str(input("Informe a data: "))
                        horario = str(input("Informe o horário: "))
                        vagas = int(input("Informe a quantidade de vagas: "))
                        valorVaga = float(input("Informe o valor da vaga: "))
                        carona = {
                           "nomeMotorista": nomeMotorista,
                           "localOrigem": localOrigem,
                           "destino": destino,
                           "data": data,
                           "horario": horario,
                           "vagas": vagas,
                           "valorVaga": valorVaga,
                            }   
                        caronas.append(carona)
                        print("Cadastra feito com sucesso")
                    elif(op == '2'):
                        print("\nLista de caronas\n")
                        for car in caronas:
                           print(f"Nome do motorista: {car["nomeMotorista"]}")
                           print(f"Local de origem: {car["localOrigem"]}")
                           print(f"Destino: {car["destino"]}")
                           print(f"Data: {car["data"]}")
                           print(f"Horario: {car["horario"]}")
                           print(f"Quantidade de vagas: {car["vagas"]}")
                           print(f"Valor da vaga: {car["valorVaga"]}")
                           print("-"*50)
                        print("\n")
                    elif(op == '3'):
                        origemBusca = input("Digite um local de origem para busca: ")
                        destinoBusca = input("Digite um destino para busca: ")
                        encontrado = False
                        for car in caronas:
                            if(origemBusca == car["localOrigem"] ):
                                encontrado = True
                                print("Encontrou a(s) carona(s)\n\n")
                                print("-"*50)
                                print(f"Nome do motorista: {car["nomeMotorista"]}")
                                print(f"Local de origem: {car["localOrigem"]}")
                                print(f"Destino: {car["destino"]}")
                                print(f"Data: {car["data"]}")
                                print(f"Horario: {car["horario"]}")
                                print(f"Quantidade de vagas: {car["vagas"]}")
                                print(f"Valor da vaga: {car["valorVaga"]}")
                                print("-"*50)
                        if(not encontrado):
                            print("Carona não existe")
                    elif(op == '0'):
                        print("Voltando ao menu cadastro")
                        break
        else:
         print("Login inválido!")
    else:
        print("Opção inválida")