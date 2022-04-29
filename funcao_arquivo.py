import time
import os
arquivo = open("numeros.txt", "w")
for linha in range(1, 101):
    arquivo.write('%d\n' %linha)
arquivo.close()
time.sleep(5)

arquivo = open("numeros.txt", "r")
for linha in range(1, 101):
    print(linha)
time.sleep(5)
arquivo.close()
