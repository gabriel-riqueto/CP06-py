import requests
import json
import os


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
        numero=input('Insira o numero: ')
        complemento=input('Insira o complemento: ')
        url=f'https://viacep.com.br/ws/{data}/json/'
        endereco=requests.get(url)

        if endereco.status_code == 200:
            dic = endereco.json()

            if len(senha) < 8:
                raise TypeError
            else:    
                cliente = {'id':id,
                        'nome':nome,
                        'email':email,
                        'senha':senha,
                        'endereço':{"rua": dic['logradouro'],
                                    "numero": numero,
                                    "complemento": complemento,
                                    "bairro": dic['bairro'],
                                    "municipio": dic['localidade'],
                                    "uf": dic['uf'],
                                    "cep": data }
                    }
                lista_clientes.append(cliente) 
                with open('clientes.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(lista_clientes, arquivo, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        print('ERRO! tem arquivo n')
    except ValueError:
        print('ERRO! id tem q ser int')
    except TypeError:
        print('A senha deve possuir ao menos 8 caracteres')
    else: 
        print('Cadastro realizado com sucesso!')

import json

def menu():
    while True:
        print("Opcão 1- Inserir")
        print("Opcão 2- Alterar")
        print("Opcão 3- Excluir")
        print("Opcão 4- Consultar")
        escolha = input("Escolha uma opção acima: ")
        if escolha == '1':
            inserir()
        elif escolha == '2':
            alterar()
        elif escolha == '3':
            print('1')
            #excluir()
        elif escolha == '4':
            print('1')
            #consultar()
        else:
            print("Por favor escolha uma oppção valida")

        return escolha
menu()
        
            

        
