
lista0 = [2, 4, 6, 7, 8, 9, 10, 12, 13, 14, 17, 18, 21, 23, 26, 27, 28, 30, 31, 34, 35, 36, 37, 40, 44, 45, 48, 52, 54, 55, 58, 59, 61, 63, 67, 72, 74, 78, 81, 83, 85, 86, 88, 91, 92, 93, 94, 97, 98, 99]
lista1 = [3, 4, 7, 8, 9, 10, 11, 12, 14, 16, 20, 23, 26, 28, 29, 32, 33, 41, 43, 45, 50, 51, 52, 54, 58, 59, 61, 63, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 78, 79, 80, 81, 82, 92, 93, 95, 96, 97, 99, 00]
lista2 = [1, 2, 5, 6, 13, 15, 17, 18, 19, 21, 22, 24, 25, 27, 30, 31, 34, 35, 36, 37, 38, 39, 40, 42, 44, 46, 47, 48, 49, 53, 55, 56, 57, 60, 62, 64, 70, 71, 76, 83, 84, 85, 86, 87, 88, 89, 90, 91, 94, 98]
lista3 = [4, 6, 7, 10, 12, 13, 17, 20, 25, 27, 33, 34, 35, 36, 38, 41, 43, 45, 46, 50, 51, 52, 54, 55, 57, 58, 59, 60, 62, 64, 66, 68, 71, 72, 74, 76, 77, 80, 81, 82, 84, 86, 87, 89, 91, 94, 95, 96, 98, 00]
lista4 = [1, 2, 3, 5, 8, 9, 11, 14, 15, 16, 18, 19, 21, 22, 23, 24, 26, 28, 29, 30, 31, 32, 37, 39, 40, 42, 44, 47, 48, 49, 53, 56, 61, 63, 65, 67, 69, 70, 73, 75, 78, 79, 83, 85, 88, 90, 92, 93, 97, 99]
lista5 = [1, 2, 4, 7, 8, 11, 13, 14, 18, 19, 24, 26, 27, 28, 29, 32, 34, 36, 38, 39, 43, 44, 49, 50, 51, 53, 61, 62, 64, 65, 67, 68, 69, 70, 73, 75, 77, 78, 81, 84, 85, 86, 87, 88, 90, 91, 92, 95, 96, 00]
lista6 = [3, 5, 6, 9, 10, 12, 15, 16, 17, 20, 21, 22, 23, 25, 30, 31, 33, 35, 37, 40, 41, 42, 45, 46, 47, 48, 52, 54, 55, 56, 57, 58, 59, 60, 63, 66, 71, 72, 74, 76, 79, 80, 82, 83, 89, 93, 94, 97, 98, 99]
lista7 = [2, 3, 4, 6, 8, 10, 11, 12, 13, 14, 18, 19, 20, 21, 22, 27, 30, 35, 38, 46, 47, 48, 49, 51, 52, 54, 56, 58, 59, 62, 64, 65, 66, 68, 69, 70, 73, 75, 76, 81, 83, 86, 88, 89, 91, 92, 96, 98, 99, 00]
lista8 = [1, 5, 7, 9, 15, 16, 17, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 36, 37, 39, 40, 41, 42, 43, 44, 45, 50, 53, 55, 57, 60, 61, 63, 67, 71, 72, 74, 77, 78, 79, 80, 82, 84, 85, 87, 90, 93, 94, 95, 97]
lista9 = [1, 3, 5, 11, 15, 16, 19, 20, 22, 24, 25, 29, 32, 33, 38, 39, 41, 42, 43, 46, 47, 49, 50, 51, 53, 56, 57, 60, 62, 64, 65, 66, 68, 69, 70, 71, 73, 75, 76, 77, 79, 80, 82, 84, 87, 89, 90, 95, 96, 00]

sorteados = [3, 11, 12, 14, 30, 31, 33, 38, 43, 44, 48, 60, 62, 64, 65, 67, 79, 85, 90, 93]
lfacil = [3, 4, 5, 6, 7, 9, 11, 13, 14, 15, 17, 20, 21, 22, 23]

facil0 = [2, 3, 4, 6, 8, 10, 12, 13, 14, 17, 18, 19, 22, 23, 24]
facil1 = [1, 2, 4, 7, 8, 9, 11, 13, 14, 15, 16, 19, 20, 22, 24]
"""
print("Tamanho listas")
print(len(sorteados))
print(len(lista0))
print(len(lista1))
print(len(lista2))
print(len(lista3))
print(len(lista4))
print(len(lista5))
print(len(lista6))
print(len(lista7))
print(len(lista8))
print(len(lista9))
"""
print("---------------------------")
print("Lotofacil 0")
contador = 0
for i in lfacil:
    if i in facil0:
        contador += 1
        print(i)
print("Total de acertos lotofacil: %s" %(contador))

print("---------------------------")
print("Lotofacil 1")
contador = 0
for i in lfacil:
    if i in facil1:
        contador += 1
        print(i)
print("Total de acertos lotofacil: %s" %(contador))

print("---------------------------")
print("---------------------------")
print("Lista 0")
contador = 0
for i in sorteados:
    if i in lista0:
        contador += 1
        print(i)
print("Total de acertos: %s" %(contador))

print("---------------------------")
print("Lista 1")
contador = 0
for i in sorteados:
    if i in lista1:
        contador += 1
        print(i)
print("Total de acertos: %s" %(contador))

print("---------------------------")
print("Lista 2")
contador = 0
for i in sorteados:
    if i in lista2:
        contador += 1
        print(i)
print("Total de acertos: %s" %(contador))

print("---------------------------")
print("Lista 3")
contador = 0
for i in sorteados:
    if i in lista3:
        contador += 1
        print(i)
print("Total de acertos: %s" %(contador))

print("---------------------------")
print("Lista 4")
contador = 0
for i in sorteados:
    if i in lista4:
        contador += 1
        print(i)
print("Total de acertos: %s" %(contador))

print("---------------------------")
print("Lista 5")
contador = 0
for i in sorteados:
    if i in lista5:
        contador += 1
        print(i)
print("Total de acertos: %s" %(contador))

print("---------------------------")
print("Lista 6")
contador = 0
for i in sorteados:
    if i in lista6:
        contador += 1
        print(i)
print("Total de acertos: %s" %(contador))

print("---------------------------")
print("Lista 7")
contador = 0
for i in sorteados:
    if i in lista7:
        contador += 1
        print(i)
print("Total de acertos: %s" %(contador))

print("---------------------------")
print("Lista 8")
contador = 0
for i in sorteados:
    if i in lista8:
        contador += 1
        print(i)
print("Total de acertos: %s" %(contador))

print("---------------------------")
print("Lista 9")
contador = 0
for i in sorteados:
    if i in lista9:
        contador += 1
        print(i)
print("Total de acertos: %s" %(contador))
