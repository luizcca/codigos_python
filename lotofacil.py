import time
d = {}
d[1] = 2, 4, 7, 8, 9, 11, 13, 15, 16, 17, 19, 20, 21, 22, 24
d[2] = 2, 4, 6, 7, 8, 9, 11, 13, 14, 16, 18, 20, 21, 22, 24

resultado = [1, 2, 3, 5, 6, 9, 10, 11, 13, 17, 18, 19, 20, 21, 25]



print("Resultado geral cartoes lotofacil 1761")
for dados in range(1,3):
        lista1 = []
        contar = 0
        for numero in resultado:
                if numero in d[dados]:
                        lista1.append(numero)
                        numero += 1
                        contar += 1
        print('Acertos: %d' %contar)
        print('Numeros no alvo: %s' %lista1)
       
