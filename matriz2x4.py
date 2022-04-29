# Program to multiply two matrices using nested loops

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6]]
# 3x4 matrix
Y = [[6,7,3,0],
     [5,8,1,2],    
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0]]

# iteracao através das linhas de X
for i in range(len(X)):
   # iteração através das colunas de Y
   for j in range(len(Y[0])):
       # iteração através das linhas de Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)

