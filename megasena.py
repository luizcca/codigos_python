import time
d = {}
d[1] = 4, 38, 41, 42, 57, 58
d[2] = 18, 22, 23, 28, 36, 54
d[3] = 7, 8, 19, 21, 25, 37
d[4] = 5, 11, 27, 35, 39, 40
d[5] = 30, 33, 43, 48, 52, 55
d[6] = 10, 15, 28, 29, 33, 46
d[7] = 8, 9, 23, 34, 51, 56
d[8] = 14, 22, 27, 31, 37, 60

resultado = [8, 14, 27, 34, 52, 54]



print("Resultado geral cartoes MEGASENA 2093")
for dados in range(1,9):
        lista1 = []
        contar = 0
        for numero in resultado:
                if numero in d[dados]:
                        lista1.append(numero)
                        numero += 1
                        contar += 1
        print('Acertos: %d' %contar)
        print('Numeros no alvo: %s' %lista1)
       
