n3 = int(input('Qual a velocidade do carro: '))
if n3 > 110:
    excedente = n3 - 110
    multa = excedente * 5
    print('Você ultrapassou o limite de velocidade em %d km' %excedente)
    print('Você foi multado em R$%5.2f' %multa)
else:
    print('Boa viagem, continue seguinte as leis de transito!')
