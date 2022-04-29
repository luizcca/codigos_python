class Empregado:
    def __init__(self,nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario
        self.email = nome + '.' + sobrenome + '@wesayso.com'

    def nomeCompleto(self):
        return "{} {}".format(self.nome, self.sobrenome)

empregado = Empregado()
for i in range(5):
    nome = input("Digite nome: ")
    sobrenome = input("Digite o sobrenome: ")
    salario = input("Digite o salario ou 0 para SAIR")
    if salario == 0:
        break
    else:
        empregado[i] = Empregado(nome, sobrenome, salario)


#emp_1 = Empregado('Luiz', 'Aguiar', 5600)
#emp_2 = Empregado('Carlos', 'Aguiar', 7800)
#print(emp_1.nomeCompleto())
print(Empregado.nomeCompleto(emp_1) + " , " + emp_1.email)
print(Empregado.nomeCompleto(emp_2) + " , " + emp_2.email)
