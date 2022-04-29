'''
for vogal in 'aeiou':
    print(vogal)
print('-----------------------------')
vogal = 'aeiou'
k = 0
while k < len(vogal):
    letra = vogal[k]
    print(letra)
    k += 1
print('-----------------------------')
for i in range(10):
    print(i)
print('-----------------------------')

lista = list(range(10))
k = 0
while k < len(lista):
    i = lista[k]
    print(i)
    k += 1
print('-----------------------------')
for x in ['cfpbr', 52, 3.14]:
    print(x)
print('-----------------------------')
'''

def épar(x):
    return x % 2 == 0


def fator(y):
    fat = 1
    while y > 0:
        fat = fat * y
        y = y - 1
    print(fat)

def embaralha(s):
    import random
    lista = list(s)
    random.shuffle(lista)
    return ''.join(lista)

def aleatorio(x,y):
    import random
    lista = []
    while len(lista) < 15:
        a = random.randint(x,y)
        if a not in lista:
            lista.append(a)
    lista.sort()
    print(lista)
    


    #Fatorial de um numero qualquer
