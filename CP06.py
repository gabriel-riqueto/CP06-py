import requests
import json
import os

#função para inserir um cliente 
def inserir():
    try:
        if os.path.exists('clientes.json'):
            with open('clientes.json', 'r', encoding='utf-8') as arquivo:
                lista_clientes = json.load(arquivo)
        else:
            lista_clientes = []
        id = int(input('Insira seu id: '))
        nome = input('Insira seu nome: ')
        email = input('Insira seu e-mail: ')
        senha = input('Insira sua senha: ')
        data = input('Insira seu CEP: ')
        numero = input('Insira o numero: ')
        complemento = input('Insira o complemento: ')
        url = f'https://viacep.com.br/ws/{data}/json/'
        endereco = requests.get(url)

        if endereco.status_code == 200:
            dic = endereco.json()

            if len(senha) < 8:
                print('A senha deve possuir pelo menos 8 caracteres')
            else:
                cliente = {'id': id,
                           'nome': nome,
                           'email': email,
                           'senha': senha,
                           'endereço': {"rua": dic['logradouro'],
                                        "numero": numero,
                                        "complemento": complemento,
                                        "bairro": dic['bairro'],
                                        "municipio": dic['localidade'],
                                        "uf": dic['uf'],
                                        "cep": data}
                           }
                lista_clientes.append(cliente)
                with open('clientes.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(lista_clientes, arquivo, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        print('ERRO! arquivo não encontrado')
    except ValueError:
        print('ERRO! id tem que ser um número inteiro')
    else:
        print('Cadastro realizado com sucesso!')

#função para alterar os dados de um cliente
def alternar():
    try:
        if os.path.exists('clientes.json'):
            with open('clientes.json', 'r', encoding='utf-8') as arquivo:
                lista_clientes = json.load(arquivo)
        else:
            print("Nenhum cliente cadastrado para atualização.")
            return

        id_cliente = int(input("Digite o ID do cliente que deseja alterar: "))

        cliente_encontrado = False

        for cliente in lista_clientes:
            if cliente['id'] == id_cliente:
                novo_nome = input("Novo nome: ")
                novo_email = input("Novo email: ")
                novo_senha = input("Nova senha: ")
                # Atualizar informações do cliente
                cliente['nome'] = novo_nome
                cliente['email'] = novo_email
                cliente['senha'] = novo_senha
                novo_cep = input("Novo CEP: ")
                url = f'https://viacep.com.br/ws/{novo_cep}/json/'
                endereco = requests.get(url)

                if endereco.status_code == 200:
                    dic = endereco.json()
                    cliente['endereço']['rua'] = dic['logradouro']
                    cliente['endereço']['numero'] = input("Novo número: ")
                    cliente['endereço']['complemento'] = input("Novo complemento: ")
                    cliente['endereço']['bairro'] = dic['bairro']
                    cliente['endereço']['municipio'] = dic['localidade']
                    cliente['endereço']['uf'] = dic['uf']
                    cliente['endereço']['cep'] = novo_cep

                cliente_encontrado = True
                break

        if cliente_encontrado:
            with open('clientes.json', 'w', encoding='utf-8') as arquivo:
                json.dump(lista_clientes, arquivo, indent=4, ensure_ascii=False)
            print(f"As informações do cliente com ID {id_cliente} foram atualizadas.")
        else:
            print(f"Cliente com ID {id_cliente} não encontrado.")

    except ValueError:
        print('ERRO! ID deve ser um número inteiro.')

#função para excluir um cliente
def excluir():
    try:
        if os.path.exists('clientes.json'):
            with open('clientes.json', 'r', encoding='utf-8') as arquivo:
                lista_clientes = json.load(arquivo)
        else:
            print("Nenhum cliente cadastrado para exclusão.")
            return

        id_cliente = int(input("Digite o ID do cliente que deseja excluir: "))

        cliente_encontrado = None

        for cliente in lista_clientes:
            if cliente['id'] == id_cliente:
                cliente_encontrado = cliente
                break

        if cliente_encontrado:
            lista_clientes.remove(cliente_encontrado)
            with open('clientes.json', 'w', encoding='utf-8') as arquivo:
                json.dump(lista_clientes, arquivo, indent=4, ensure_ascii=False)
            print(f"Cliente com ID {id_cliente} foi excluído com sucesso.")
        else:
            print(f"Cliente com ID {id_cliente} não encontrado.")

    except ValueError:
        print('ERRO! ID deve ser um número inteiro.')

#função para mostrar todods os clientes
def consultar():
    try:
        if os.path.exists('clientes.json'):
            with open('clientes.json', 'r', encoding='utf-8') as arquivo:
                lista_clientes = json.load(arquivo)

            if len(lista_clientes) == 0:
                print("Nenhum cliente cadastrado.")
            else:
                print("Lista de clientes:")
                for cliente in lista_clientes:
                    print("-------------")
                    print(f"ID: {cliente['id']}")
                    print(f"Nome: {cliente['nome']}")
                    print(f"E-mail: {cliente['email']}")
                    print(f"CEP: {cliente['endereço']['cep']}")
                    print("-------------")
        else:
            print("Nenhum cliente cadastrado.")
    except FileNotFoundError:
        print('ERRO! Arquivo não encontrado.')
#menu
def menu():
    while True:
        print("Opção 1- Inserir")
        print("Opção 2- Alterar")
        print("Opção 3- Excluir")
        print("Opção 4- Consultar")
        print("Opção 0- Sair")
        escolha = input("Escolha uma opção acima: ")
        
        if escolha == '1':
            inserir()
        elif escolha == '2':
            alternar()
        elif escolha == '3':
            excluir()
        elif escolha == '4':
            consultar()
        elif escolha == '0':
            print("Encerrando o programa.")
            break 
        else:
            print("Por favor escolha uma opção válida")
menu()