class Linha():
    def __init__(self, x1 = 2, x2 = 3, y1 = 1, y2 = 1):
        self.X1 = x1
        self.X2 = x2
        self.Y1 = y1
        self.Y2 = y2

    def calculo(self):
        deltax = self.X2 - self.X1
        deltay = self.Y2 - self.Y1
        P0 = 2 * deltay - 2 * deltax        
        Pk = 2 * deltay - deltax
        return "{0:5} {1:5} {2:5} {3:5}".format(deltax, deltay, P0, Pk)
        '''
        result = []
        for i in range(x2 - x1):
        '''


l = Linha(20, 30, 10, 18)
print(l.calculo())
