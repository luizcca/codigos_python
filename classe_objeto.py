class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2

>>> tv_quarto = Televisão()
>>> tv_sala = Televisão()
>>> tv_quarto.ligada
False
>>> tv_quarto.canal
2
>>> tv_quarto.ligada = True
>>> tv_quarto.ligada
True
>>> tv_quarto.canal = 7
>>> tv_quarto.canal
7
>>> 
