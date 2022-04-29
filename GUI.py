from tkinter import *

janela = Tk()
largura_janela = 800
altura_janela = 800

largura_monitor = janela.winfo_screenwidth()
altura_monitor = janela.winfo_screenmmheight()

coordenada_x = (largura_monitor/2) - (largura_janela/2)
coordenada_y = (altura_monitor/2) - (altura_janela/2)

janela.title("Demo de GUI em Pythom")

janela.geometry("{0}x{1}+{2}+{3}".format(largura_janela,altura_janela,coordenada_x,coordenada_y))

janela.resizable(width=False, height=False)

janela.mainloop()
