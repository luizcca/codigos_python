#àrvore de busca binaria em Python

class Node:
    def __init__ (self, val):
        self.value = val
        self.filhoEsquerda = None
        self.filhoDireita = None

    def insert (self, data):
        if self.value == data:
             return False
        elif self.value > data:
                if self.filhoEsquerda:
                    return self.filhoEsquerda.insert(data)
                else:
                    self.filhoEsquerda = Node(data)
                    return True
        else:
            if self.filhoDireita:
                return self.filhoDireita.insert(data)
            else:
                self.filhoDireita = Node(data)
                return True

    def find (self, data):
        if(self.value == data):
            return True
        elif self.value > data:
            if self.filhoEsquerda:
                return self.filhoEsquerda.find(data)
            else:
                return False
        else:
            if self.filhoDireita:
                return self.filhoDireita.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print (str(self.value))
            if self.filhoEsquerda:
                self.filhoEsquerda.preorder()
            if self.filhoDireita:
                self.filhoDireita.preorder()

    def postorder(self):
        if self:
            if self.filhoEsquerda:
                self.filhoEsquerda.postorder()
            if self.filhoDireita:
                self.filhoDireita.postorder()
            print (str(self.value))

    def inorder(self):
        if self:
            if self.filhoEsquerda:
                self.filhoEsquerda.inorder()
            print (str(self.value))
            if self.filhoDireita:
                self.filhoDireita.inorder()
            
            


class Tree:
    def __init__ (self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def finf(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print("Pré Ordem")
        self.root.preorder()

    def postorder(self):
        print("Pós Ordem")
        self.root.postorder()

    def inorder(self):
        print("Em Ordem")
        self.root.inorder()


bst = Tree()
print(bst.insert(10))
print(bst.insert(15))
print(bst.insert(15))
print(bst.insert(15))
print(bst.insert(8))
print(bst.insert(9))
print(bst.insert(16))
print(bst.finf(7))
print(bst.finf(8))
bst.preorder()
bst.postorder()
bst.inorder()

    
