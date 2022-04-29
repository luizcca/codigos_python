import time
'''
a = int(input('a: '))
b = int(input('b: '))
k = 1

while a % b != 0:
    a, b = b, a%b

print('mdc = %d' %b)

edificio = ['Familia Silva','Familia Souza','Familia Tanaka','Familia Aguiar']

edificio.append('Familia Furtado')
edificio.append('Familia Americo')
edificio[5] = 'Familia Chagas'

for familia in edificio:
    print(familia)
    time.sleep(5)


notas = [7, 8.3, 6.8, 7.4, 5]

soma = 0
i = 4 
while i >= 0:
    soma += notas[i]
    i -= 1
media = soma / 5
print('A média é: %2.2f' %media)


notas = []
soma = 0
i = 0

while i < 5:
    nota = float(input('Digite a %dº nota: ' %(i+1)))
    notas.append(nota)
    i += 1
i = i-1
while i >= 0:
    soma += notas[i]
    print('A soma é: %2.2f' %soma)
    time.sleep(2)
    i -= 1
media = soma / 5
print('A média é: %2.2f' %media)
print('As notas foram: ', notas)


notas = []
i = 0

while i < 10:
    nota = float(input('Digite a %dº nota: ' %(i+1)))
    notas.append(nota)
    i += 1
i = i-1
print('Notas na ordem inversa:')
while i >= 0:
    print(notas[i])
    time.sleep(2)
    i -= 1
print('Fim!')
'''

letras = []
i = 0
tot_cons = 0

while i < 10:
    letra = input('Digite a %dª letra: ' %(i+1))
    letras.append(letra)
    i += 1
i -= 1
while i >= 0:
    if letras[i] not in 'aeiou':
        tot_cons += 1
    i -= 1
print('Total de consoantes minusculas é: %d' %tot_cons)

# total de consoantes minusculas
