d = {}
d[1] = 3, 5, 6, 9, 10, 12, 15, 16, 17, 20, 21, 22, 23, 25, 30, 31, 33, 35, 37, 40, 41, 42, 45, 46, 47, 48, 52, 54, 55, 56, 57, 59, 60, 63, 66, 71, 72, 74, 76, 79, 80, 82, 83, 89, 92, 93, 94, 97, 98, 99
d[2] = 1, 2, 3, 5, 8, 9, 11, 14, 15, 16, 18, 19, 21, 22, 23, 24, 26, 28, 29, 30, 31, 32, 37, 39, 40, 42, 44, 47, 48, 49, 53, 56, 61, 63, 65, 67, 69, 70, 73, 75, 78, 79, 83, 85, 88, 90, 92, 93, 97, 99
d[3] = 1, 2, 5, 6, 13, 15, 17, 18, 19, 21, 22, 24, 25, 27, 30, 31, 34, 35, 36, 37, 38, 39, 40, 42, 44, 46, 47, 48, 49, 53, 55, 56, 57, 60, 62, 64, 70, 71, 76, 83, 84, 85, 86, 87, 88, 89, 90, 91, 94,98
d[4] = 2, 4, 6, 7, 8, 9, 10, 12, 13, 14, 17, 18, 21, 23, 26, 27, 28, 30, 31, 34, 35, 36, 37, 40, 44, 45, 48, 52, 54, 55, 58, 59, 61, 63, 67, 72, 74, 78, 81, 83, 85, 86, 88, 91, 92, 93, 94, 97, 98, 99
d[5] = 1, 5, 7, 9, 15, 16, 17, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 36, 37, 39, 40, 41, 42, 43, 44, 45, 50, 53, 55, 57, 60, 61, 63, 67, 71, 72, 74, 77, 78, 79, 80, 82, 84, 85, 87, 90, 93, 94, 95,97 

resultado = [11, 14, 26, 28, 29, 30, 36, 46, 47, 48, 62, 73, 80, 83, 84, 85, 86, 88, 95, 98]



print("Resultado geral cartoes lotomania 1934")
for dados in range(1,6):
        lista1 = []
        contar = 0
        for numero in resultado:
                if numero in d[dados]:
                        lista1.append(numero)
                        numero += 1
                        contar += 1
        print('Acertos: %d' %contar)
        print('Numeros no alvo: %s' %lista1)



    
