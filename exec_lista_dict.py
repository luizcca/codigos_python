import tempo_exec_lista_dicionario
import time

t0 = time.time()
read_dataset_list()
t1 = time.time()
dados = t1 - t0
print("Arquivo de dados criado em {} segundos\n".format(dados))

t0 = time.time()
read_dataset_list()
t1 = time.time()
lista = t1 - t0
print("Lista criada em {} segundos\n".format(lista))

t0 = time.time()
read_dataset_list()
t1 = time.time()
dicionario = t1 - t0
print("Dicionario criado em {} segundos\n".format(dicionario))

f = open("dados.xls", "w")
f.write("{:> 10} {:> 10} {:> 10}\n".format(dados, lista, dicionario))
f.close()
