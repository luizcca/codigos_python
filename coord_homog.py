x= int(input("coordenada x: "))
y= int(input("coordenada y: "))
tx=float(input("translação em x: "))
ty=float(input("translação em y: "))
'''
teta=int(input("angulo de rotação: "))
ex=int(input("escalar de x: "))
ey=int(input("escalar de y: "))
'''


M = [x,y,1]

def transposta_b(mat):
    """Transposta de uma matriz."""
    return [list(linha) for linha in mat]

aux = transposta_b(M)

#translação
t = [[0,0,-tx],[0,0,-ty],[0,0,1]]

#resultado
resultado = [[0,0,0],[0,0,0],[0,0,0]]

# iterate sobre linhas de aux
for i in range(len(aux)):
    # iterate sobre columnas de Y
    for j in range(len(t[0])):
        # iterate sobre linhas de Y
        for k in range(len(t)):
            resultado[i][j] += aux[i][k] * t[k][j]

print("MATRIZ RESULTANTE")
for r in resultado:
    print(r)

