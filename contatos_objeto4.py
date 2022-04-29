"""
contatos4.py
Este programa ajuda a gerenciar meus contatos.
@autor Luiz Aguiar
@versao 12/03/2018
"""
class Person(object):
    """
    A classe Person define uma pessoa em termos de:
    nome, telefone e endereço de email.
    """
    #Construtor
    def __init__(self, Name, Fone, Email):
        self.name = Name
        self.fone = Fone
        self.email = Email
    
    #Métodos de acesso(getters)
    def getName(self):
        return self.name

    def getFone(self):
        return self.fone

    def getEmail(self):
        return self.email

    
    #Metodos de alteração(mutator) (setters)
    def setFone(self,novoTelefone):
        self.fone = novoTelefone

    def setEmail(self, novoEmail):
        self.email = novoEmail
        
    def __str__(self):
        return '{0:10s} {1:10s} {2:10s}'.format(self.name,self.fone,self.email)

def enter_a_friend():
    name = input("Enter friend's name: ")
    fone = input("Enter a fone number: ")
    email = input("Enter email address: ")
    return Person(name,fone,email)

def busca_um_amigo(friends):
    achado = False
    name = input("Entreo nome a buscar: ")
    for friend in friends:
        if name in friend.getName():
            print(friend)
            found = True
    if not found:
        print("Você não possui amigo(s) com este nome")

def show_all_friends(friends):
    print("Mostrando todos os amigos:")
    for friend in friends:
        print(friend)

def main():

    friends = []
    running = True
    while running:
        print("\nGerenciador de Contatos")
        print("1) novo contato     2) buscar contato")
        print("3) mostrar contatos 4) sair")
        opcao = input("> ")
        if opcao == "1":
              friends.append(enter_a_friend())
        elif opcao == "2":
              busca_um_amigo(friends)
        elif opcao == "3":
              show_all_friends(friends)
        elif opcao == "4":
              running = False
        else:
              print("Entrada incorreta. Favor tente novamente.")
    print("Encerrando programa.")
              

if __name__ == "__main__":
    main()
