class Empregado(object):

    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario
        self.email = nome + "." + sobrenome + '@wesayso.com'
        self.next = None

class LinkedList(object):

    def __init__(self):
        self.iniciar = None

    def add_node(self, nome, sobrenome, salario):
        node = Empregado(nome, sobrenome, salario)
        if not self.iniciar:
            self.iniciar = node
            return

        mover = self.iniciar
        while(mover.next):
            mover = mover.next
        mover.next = node

    def imprimir(self):
        mover = self.iniciar
        print("{: >20}{: >20}{: >30}{: >20}".format("Nome","Sobrenome","Email","Salario"))
        while(mover):
            print("{: >20}{: >20}{: >30}{: >20}".format(mover.nome.upper(),mover.sobrenome.upper(), mover.email.upper(), "R$ " + str(mover.salario)))
            mover = mover.next

class Gerente(Empregado):
    pass

print(help(Gerente))

"""
linkedList = LinkedList()
i = 0
print("Digite 0 para sair ou comece a cadastrar o EMPREGADO: ")
while i == 0:
    nome = input("Insira o nome: ")
    if nome == '0':
        i = 1
    else:
        sobrenome = input("Insira o sobrenome: ")
        salario = float(input("Insira o salario: "))
        linkedList.add_node(nome, sobrenome, salario)


linkedList.imprimir()
"""

"""
SITE PYTHON TUTOR: LINK PERMANENT
http://pythontutor.com/visualize.html#code=class%20Empregado(object%29%3A%0A%0A%20%20%20%20def%20__init__(self,%20nome,%20sobrenome,%20salario%29%3A%0A%20%20%20%20%20%20%20%20self.nome%20%3D%20nome%0A%20%20%20%20%20%20%20%20self.sobrenome%20%3D%20sobrenome%0A%20%20%20%20%20%20%20%20self.salario%20%3D%20salario%0A%20%20%20%20%20%20%20%20self.next%20%3D%20None%0A%0Aclass%20LinkedList(object%29%3A%0A%0A%20%20%20%20def%20__init__(self%29%3A%0A%20%20%20%20%20%20%20%20self.iniciar%20%3D%20None%0A%0A%20%20%20%20def%20add_node(self,%20nome,%20sobrenome,%20salario%29%3A%0A%20%20%20%20%20%20%20%20node%20%3D%20Empregado(nome,%20sobrenome,%20salario%29%0A%20%20%20%20%20%20%20%20if%20not%20self.iniciar%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.iniciar%20%3D%20node%0A%20%20%20%20%20%20%20%20%20%20%20%20return%0A%0A%20%20%20%20%20%20%20%20mover%20%3D%20self.iniciar%0A%20%20%20%20%20%20%20%20while(mover.next%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20mover%20%3D%20mover.next%0A%20%20%20%20%20%20%20%20mover.next%20%3D%20node%0A%0A%20%20%20%20def%20imprimir(self%29%3A%0A%20%20%20%20%20%20%20%20mover%20%3D%20self.iniciar%0A%20%20%20%20%20%20%20%20print(%22%7B%3A%20%3E15%7D%7B%3A%20%3E15%7D%7B%3A%20%3E15%7D%22.format(%22Nome%22,%22Sobrenome%22,%22Salario%22%29%29%0A%20%20%20%20%20%20%20%20while(mover%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print(%22%7B%3A%20%3E15%7D%7B%3A%20%3E15%7D%7B%3A%20%3E15%7D%22.format(mover.nome.upper(%29,%20mover.sobrenome.upper(%29,%20%22R%24%20%22%20%2B%20mover.salario%20%2B%20%22,00%22%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20mover%20%3D%20mover.next%0A%0AlinkedList%20%3D%20LinkedList(%29%0Ai%20%3D%200%0Aprint(%22Digite%200%20para%20sair%20ou%20comece%20a%20cadastrar%20o%20EMPREGADO%3A%20%22%29%0Awhile%20i%20%3D%3D%200%3A%0A%20%20%20%20nome%20%3D%20input(%22Insira%20o%20nome%3A%20%22%29%0A%20%20%20%20if%20nome%20%3D%3D%20'0'%3A%0A%20%20%20%20%20%20%20%20i%20%3D%201%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20sobrenome%20%3D%20input(%22Insira%20o%20sobrenome%3A%20%22%29%0A%20%20%20%20%20%20%20%20salario%20%3D%20input(%22Insira%20o%20salario%3A%20%22%29%0A%20%20%20%20%20%20%20%20linkedList.add_node(nome,%20sobrenome,%20salario%29%0A%0A%0AlinkedList.imprimir(%29%0A&cumulative=false&curInstr=86&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%22luiz%20carlos%22,%22aguiar%22,%221200%22,%22carlos%20alberto%22,%22aguiar%22,%221400%22,%22emilia%20maria%22,%22aguiar%22,%221500%22,%220%22%5D&textReferences=false
versao com email
http://pythontutor.com/visualize.html#code=class%20Empregado(object%29%3A%0A%0A%20%20%20%20def%20__init__(self,%20nome,%20sobrenome,%20salario%29%3A%0A%20%20%20%20%20%20%20%20self.nome%20%3D%20nome%0A%20%20%20%20%20%20%20%20self.sobrenome%20%3D%20sobrenome%0A%20%20%20%20%20%20%20%20self.salario%20%3D%20salario%0A%20%20%20%20%20%20%20%20self.email%20%3D%20nome%20%2B%20%22.%22%20%2B%20sobrenome%20%2B%20'%40wesayso.com'%0A%20%20%20%20%20%20%20%20self.next%20%3D%20None%0A%0Aclass%20LinkedList(object%29%3A%0A%0A%20%20%20%20def%20__init__(self%29%3A%0A%20%20%20%20%20%20%20%20self.iniciar%20%3D%20None%0A%0A%20%20%20%20def%20add_node(self,%20nome,%20sobrenome,%20salario%29%3A%0A%20%20%20%20%20%20%20%20node%20%3D%20Empregado(nome,%20sobrenome,%20salario%29%0A%20%20%20%20%20%20%20%20if%20not%20self.iniciar%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.iniciar%20%3D%20node%0A%20%20%20%20%20%20%20%20%20%20%20%20return%0A%0A%20%20%20%20%20%20%20%20mover%20%3D%20self.iniciar%0A%20%20%20%20%20%20%20%20while(mover.next%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20mover%20%3D%20mover.next%0A%20%20%20%20%20%20%20%20mover.next%20%3D%20node%0A%0A%20%20%20%20def%20imprimir(self%29%3A%0A%20%20%20%20%20%20%20%20mover%20%3D%20self.iniciar%0A%20%20%20%20%20%20%20%20print(%22%7B%3A%20%3E20%7D%7B%3A%20%3E20%7D%7B%3A%20%3E30%7D%7B%3A%20%3E20%7D%22.format(%22Nome%22,%22Sobrenome%22,%22Email%22,%22Salario%22%29%29%0A%20%20%20%20%20%20%20%20while(mover%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print(%22%7B%3A%20%3E20%7D%7B%3A%20%3E20%7D%7B%3A%20%3E30%7D%7B%3A%20%3E20%7D%22.format(mover.nome.upper(%29,mover.sobrenome.upper(%29,%20mover.email.upper(%29,%20%22R%24%20%22%20%2B%20str(mover.salario%29%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20mover%20%3D%20mover.next%0A%0Aclass%20Gerente(Empregado%29%3A%0A%20%20%20%20pass%0A%0A%0AlinkedList%20%3D%20LinkedList(%29%0Ai%20%3D%200%0Aprint(%22Digite%200%20para%20sair%20ou%20comece%20a%20cadastrar%20o%20EMPREGADO%3A%20%22%29%0Awhile%20i%20%3D%3D%200%3A%0A%20%20%20%20nome%20%3D%20input(%22Insira%20o%20nome%3A%20%22%29%0A%20%20%20%20if%20nome%20%3D%3D%20'0'%3A%0A%20%20%20%20%20%20%20%20i%20%3D%201%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20sobrenome%20%3D%20input(%22Insira%20o%20sobrenome%3A%20%22%29%0A%20%20%20%20%20%20%20%20salario%20%3D%20float(input(%22Insira%20o%20salario%3A%20%22%29%29%0A%20%20%20%20%20%20%20%20linkedList.add_node(nome,%20sobrenome,%20salario%29%0A%0A%0AlinkedList.imprimir(%29&cumulative=false&curInstr=65&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%22luiz%22,%22aguiar%22,%221200%22,%22carlos%22,%22aguiar%22,%221400%22,%220%22%5D&textReferences=false
"""
