arq = open("notas_estudantes.dat","r")

for linha in arq:
    linhas = linha.split()
    if len(linhas) > 7:
        print(linhas[0])

arq.close()

arq = open("notas_estudantes.dat","r")

for linha in arq:
    linhas = linha.split()
    for linhas[1] ) > 7:
        print(linhas[0])

arq.close()
