m=int(input("linhas Matriz 1: "))
n=int(input("coluna Matriz 1: "))
p=int(input("linhas Matriz 2: "))
q=int(input("colunas Matris 2: "))

if n == p:
    X = []
    print("PRIMEIRA MATRIZ")
    for i in range (m):
        m1=[]
        print("linha{}".format(i+1))
        for j in range (n):
            m1.append(int(input("A{}: ".format(j+1))))
        X.append(m1)

    Y = []
    print("SEGUNDA MATRIZ")
    for i in range (p):
        n1=[]
        print("linha{}".format(i+1))
        for j in range (q):
            n1.append(int(input("B{}: ".format(j+1))))
        Y.append(n1)

    resultado = []
    for i in range (m):
        q1=[]
        for j in range (q):
            q1.append(0)
        resultado.append(q1)

    print("MATRIZ NULA")
    for r in resultado:
        print(r)

    # iterate sobre linhas de X
    for i in range(len(X)):
        # iterate sobre columnas de Y
        for j in range(len(Y[0])):
            # iterate sobre linhas de Y
            for k in range(len(Y)):
                resultado[i][j] += X[i][k] * Y[k][j]

    print("MATRIZ RESULTANTE")
    for r in resultado:
        print(r)

else:
    print("Matrizes não podem ser multiplicadas!")
