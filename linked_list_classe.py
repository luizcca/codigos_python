class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index == self.length():
            print("ERRO: Indice fora da lista!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index: return cur_node.data
            cur_idx += 1
                  
        

my_list = linked_list()

my_list.display()

my_list.append("Pedro")
my_list.append("Paulo")
my_list.append("Santos")
my_list.append("Oliveira")
my_list.append("Silva")

my_list.display()

print("O terceiro elemento da lista é: {}".format(my_list.get(2)))


        
