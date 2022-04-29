from graphics import *

def main():
    win = GraphWin("Minha janela Grafica", 500, 500)
    win.setBackground('white')
    ganho = 50
    cor1 = 80
    cor2 = 80
    cor3 = 80
    
    for i in range(40):
        b = 3 * i
        pt = Point(ganho,ganho)
        cir = Circle(pt,50)
        cir.setFill(color_rgb(cor1+b,cor2+b,cor3+b))
        cir.draw(win)
        ganho += 4
        i += 1
    win.getMouse()
    win.close()


main()
