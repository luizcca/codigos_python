lista0 = [2, 4, 6]

sorteados = [1, 2]

acertos = []
contador = 0
for i in sorteados:
    if i in lista0:
        contador += 1
        print(i)
