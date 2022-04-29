def aleatorios_entre_10_e_100():
    import random
    i = 0
    count = 0
    lista = [50]
    while i < 50:
        x = random.randint(0, 100)
        count += 1
        lista.append(x)
        print (x," ")
        i += 1
    print("Foram gerados %d numeros" %count)
    lista

aleatorios_entre_10_e_100()

