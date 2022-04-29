def addMatrix(A,B):
    """ Soma duas matrizes."""
    sizeL=len(A)
    sizeC=len(A[0])
    C=nullMatrix(sizeL,sizeC)
    # Soma
    for i in range(sizeL):
        for j in range(sizeC):
            C[i][j]=A[i][j]+B[i][j]
    return C

 

def prodMatrix(A,B):
    """Multiplica duas matrizes."""
    sizeL=len(A)
    sizeC=len(A[0])
    C=nullMatrix(sizeL,sizeC)
    # Multiplica
    for i in range(sizeL):
        for j in range(sizeC):
            val=0
            for k in range(len(B[0])):
                val = val + A[i][k]*B[k][j]
            C[i][j]=val
    return C

 

def transposeMatrix(M):
    """Calcula a transposta de uma matriz."""
    aux=[]
    for j in range(len(M[0])):
        linha=[]
        for i in range(len(M)):
            linha.append(M[i][j])
        aux.append(linha)
    return aux



import random
 

def cria_matriz(lin,col):
    A=[]
    for i in range(lin):
        linha=[]
        for j in range(col):
            linha = linha + [random.randint(1,10)]
        A= A + [linha]
    return A
 

def mostra_matriz(matriz):
    print ('Matriz')
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print (matriz[i][j],sep=" ")
        print()
    print ('_' * 10)




mostra_matriz(cria_matriz(3,3))
