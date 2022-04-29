class Ponto:
    """Esta é uma classe para demonstração.

Este documento é um docstring
que é usado para documentar a classe
    """
    pass

print(Ponto.__doc__)
print("*********************************")

p1 = Ponto()
print(p1.__doc__)

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print(dir(p1))
print(type(p1))
print(id(p1))
print(p1.x)
print(p1.y)
