import random
class Dado:
    """Esta é uma classe para demonstração.

Este documento é um docstring
que é usado para documentar a classe
"""
    def __init__(self):
        self.lado = 0
    
    def lancar(self):
        self.lado = random.randint(1, 6)

    def get_valor(self):
        return self.lado



meu_dado = Dado()
verdade = True
while verdade:
    print("O valor atual é: {}".format(meu_dado.get_valor()))
    continuar = input("Continuar jogando(S/N): ")
    if continuar == 'N' or continuar == 'nao':
        verdade = False
    else:
        meu_dado.lancar()
        print("O novo valor da face é: {}".format(meu_dado.get_valor()))



