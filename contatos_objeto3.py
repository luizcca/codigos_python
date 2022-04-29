"""
contatos3.py
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



def main():

    friend1 = Person("Jill", "555-1254", "jbush@gmail.org")
    friend2 = Person("Carlos", "555-5248", "carlos222@gmail.org")
    friend3 = Person("Paulo", "555-1458", "pauloas@gmail.org")
    print(friend1.getEmail())
    friend1.setEmail("jbush@gmail.com")
    print(friend1.getEmail())
    print(friend1)
    print(friend2)
    print(friend3)

if __name__ == "__main__":
    main()
