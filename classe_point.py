class text1:
    pass

class point:
    def __init__(self,x = 0, y = 0, z = 0):
        self.atribuir(x, y, z)

    def atribuir(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def printPoint(self):
        print("{0:^10}{1:^10}{2:^10}".format(self.x, self.y, self.z))
    

'''
p1 = point()
p1.x = 2
p1.y = 3
p1.z = 5
'''
a = 'VARX'
b = 'VARY'
c = 'VARZ'

print("{0:^10}{1:^10}{2:^10}".format(a, b, c))
p1 = point(2, 3, 5)
#p1.atribuir(2, 3, 5)
p1.printPoint()


p2 = point(6, 2, -4)
#p2.atribuir(6, 2, -4)
p2.printPoint()

p3 = point()
p3.printPoint()
print(type(p3))

print('\n\n\n')

for x in range(1, 11):
    print('{0:5d} {1:5d} {2:5d} {3:5d}'.format(x, x**2, x**3, x**4))


'''
p2 = point()
p2.x = 6
p2.y = 2
p2.z = -4

#print(p1)
#print(p1.x, p1.y, p1.z)
#print(p2)
#print(p2.x, p2.y, p2.z)

t1 = text1()
t1.test1 = "Hello world!"

t1.var1 = 3.14

print(t1.test1)
print(t1.var1)
'''
