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

def épar(x):
    return x % 2 == 0

def fatorial(y):
    n = 1
    fat = 1
    x = int(y)
    while n <= x:
        fat = fat * n
        n = n + 1
    print('Fatorial de %d é: %d' %(n-1,fat))
    #Fatorial de um numero qualquer
