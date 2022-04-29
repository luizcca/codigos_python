"""
contatos1.py
Este programa ajuda a gerenciar meus contatos.
@autor Luiz Aguiar
@versao 12/03/2018
"""

def main():

    friends = []

    for i in range(2):
        print("gerenciar contatos")
        name = input('Entre o nome: ')
        telefone = input('Entre o telefone: ')
        email = input('Entre o email: ')
        friends.append([name, telefone, email])

    for i in range(len(friends)):
        print('Informação de contatos')
        for j in range(len(friends[1])):
            print(friends[i][j])



if __name__ == "__main__":
    main()
