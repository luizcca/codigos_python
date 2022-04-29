import random

aprocurar = random.randint(1, 150)
tentativas = 0
numero = 0

while numero != aprocurar:
    numero = int(input("Escolha um numero entre 0 e 150: "))
    tentativas += 1
    if numero > aprocurar:
        print ("Menor")
    elif numero < aprocurar:
        print ("Maior")

print("Voce acertou o numero é: %d" %numero)
print ("Voce fez %d tentativas" %tentativas)
