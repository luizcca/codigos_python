import csv
class Node:
  def __init__(self,chave,acess,altura):
    self.left = None
    self.right = None
    self.chave = chave
    self.acess = acess
    self.altura = altura


class BinaryTree(Node):
  def __init__(self):
    self.root = None

  def addNode(self,chave,acess,altura):
    return Node(chave,acess,altura)

  def insert(self,root,chave,acess,altura):
    if(root == None):
      root = self.addNode(chave,acess,altura)
    else:
      altura += 1
      if(chave <= root.chave):
        root.left = self.insert(root.left,chave,acess,altura)
      else:
        root.right = self.insert(root.right,chave,acess,altura)
    return root

  def CustoArvore(self,root):
    if root == None:
      return 0
    else:
        custo = (root.acess * root.altura)
        x = (self.CustoArvore(root.left))
        custo = custo + x
        y = (self.CustoArvore(root.right))
        custo = custo + y

        return custo

a = BinaryTree()
menorCusto = 1000000000
ifile  = open('base2.txt', "r")
read = csv.reader(ifile, delimiter=';')
x = []
N = 5 #quantidade de dados lidos da tabela
for [acessos,dominios] in read:
        x.append(int(acessos))


for i in range(N):
    root = a.addNode(i,x[i],1)
    for j in range(N):
        if(i != j):
            a.insert(root,j,x[j],1)
    print("Arvore ",i+1,": ",a.CustoArvore(root))
    if(menorCusto > a.CustoArvore(root) ):
        menorCusto = a.CustoArvore(root)

print("menor custo:",menorCusto)

z = input()
ifile.close()
exit()
