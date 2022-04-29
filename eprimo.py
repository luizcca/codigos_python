soma = 0
divisores = []
primo = int(input("Insira um numero a ser testado: "))
for i in range(1, primo+1):
    if primo % i == 0:
        soma += 1
        divisores.append(i)
if soma > 2:
    print("O numero {} não é primo.".format(primo))
    print("Os divisores de {} são: {}".format(primo, divisores))
else:
    print("O numero {} é primo.".format(primo))
    print("Os divisores de {} são: {}".format(primo, divisores))
