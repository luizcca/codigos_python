#import random
"""
v = int(input("velocidade: "))
if v > 110:
    print("Você será multado em: R$ %d,00" %((v-110)*5))
else:
    print("Pode viajar sem medo.")
"""
"""
conta = 0
menor200 = 0.20
menor400 = 0.18
maior400 = 0.15
maior800 = 0.08
v = int(input("Minutos utilizados: "))
if v <= 200:
    conta = conta + v * menor200
elif v <= 400:
    conta = conta + v * menor400
elif v <= 800:
    conta = conta + v * maior400
else:
    conta = conta + v * maior800
    print("Acima de 800min sua conta telefonica custa R$0.08 por minuto e será: R$ %5.2f" %conta)

print("Sua conta telefonica é: R$ %5.2f" %conta)
"""
"""
a = int(input("Primeiro: "))
b = int(input("Segundo: "))
c = int(input("Terceiro: "))

if a >= b and b >= c:
    print ("Maior valor é: %d" %a)
    print ("Valor do meio é: %d" %b)
    print ("menor valor é: %d" %c)
if a > b and c >= b:
    print ("Maior valor é: %d" %a)
    print ("Valor do meio é: %d" %c)
    print ("menor valor é: %d" %b)
else:
    print ("O terceiro maior valor é: %d" %c)

v = 0
n = int(input("Insira um numero: "))
while v <= n:
    if v % 2 == 1:
        print(v)
    v = v + 1

n = 1
soma = 0
while n <= 10:
    x = int(input("Insira o %d numero: " %n))
    soma = soma + x
    n = n + 1
media = float( soma / 10)
print("Soma: %d" %soma)
print("Media: %5.2f" %media)

*****************************
soma = 0
n = -2
contador = 1
while n != -1:
    x = int(input("Insira um numero: "))
    soma = soma + x
    resp = input("Inserir outro numero?(S (para SIM) ou qualquer letra para sair): ")
    if resp == "S" or resp == "s":
        contador = contador + 1
    else:
        n = -1
        
media = float( soma / contador)
print ("Contador: %d" %contador)
print("Soma: %d" %soma)
print("Media: %5.2f" %media)
*******************************

soma = 0
contador = 0
while True:
    x = int(input("Insira um numero ou 0 para sair: "))
    if x == 0:
        break
    soma = soma + x
    contador = contador + 1

media = float( soma / contador)
print ("Contador: %d" %contador)
print("Soma: %d" %soma)
print("Media: %5.2f" %media)
*******************************
"""   
#SEQUENCIA DE FIBONACCI
"""
a b a+b
1 1 2
1 2 3
2 3 5
3 5 8
5 8 13

n = int(input("Insira um numero: "))
a, b = 1, 1
k = 1

while k <= n - 2:
    a, b = b, a + b
    k = k + 1

print("Fibonacci(%d) = %d " %(n, b))
"""
#ALGORITMO DE EUCLIDES
"""
a b a%b
21 15 6
15 6  3
6  3  0

a = int(input("a: "))
b = int(input("b: "))

while a % b != 0:
    a, b = b, a % b

print ("mdc = %d" %b)


#LISTAS EM PYTHON

lista = []
x = 1
while x < 10:
    n = int (input("Digite um numero: "))
    lista.append(n)
    x += 1
print ("Conteúdo da lista:", lista)

#LISTAS EM ORDEM DIRETA e INVERSA EM PYTHON

lista = []
inversa = []
x = 1
y = 3
while x < 5:
    n = int (input("Digite um numero: "))
    lista.append(n)
    x += 1
print ("Conteúdo da lista:", lista)
while y >= 0:
    inversa.append(lista[y])
    y -= 1
print ("Conteúdo da lista inversa:", inversa)

"""
import random
lista = random.sample(range(1, 100), 50)

print("Lista gerada com uso do metodo SAMPLE de RANDOM")
print(lista)
print('\n\n')

for i in range(0, 50):
    for j in range (1, 50):
        if lista[j-1] > lista[j]:
            x = lista[j-1]
            lista[j-1] = lista[j]
            lista[j] = x
print("Lista ordenado com uso do algoritmo BUBLESORT")
print(lista)
    
