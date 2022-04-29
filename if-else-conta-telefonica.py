t = True
while t:
    m = float(input('Minutos usados: '))
    if (m < 200):
        cobrar = m * 0.2
    elif m < 400:
       cobrar = m * 0.18
    elif m <= 800:
       cobrar = m * 0.15
    else:
        cobrar = m * 0.08
    print('Sua conta telefonica é de R$%5.2f' %cobrar)
    Resposta = input('Realizar uma nova cobrança(S/N)? ')
    if (Resposta == 'N' or Resposta == 'n'):
        t = False

'''
A empresa tarifa facil cobra de seus usuarios segundo as faixas abaixo,
calcule o valor a cobrar de acordo com as faixas:
menos de 200 minutos, 0,20 por minuto;
entre 200 e 400 minutos, 0,18 por minuto;
entre 400 e 800 minutos, 0,15 ppor minuto;
acima de 800 minutos 0,08 por minuto
'''
