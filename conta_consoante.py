def conta_vogal():
    palavra = []
    i = 0
    while i < 10:
        letra = input('Digite uma letra: ')
        if len(letra) == 1:
            palavra += letra
            i += 1
        else:
            print('Você digitou mais de uma letra')
            print('Reiniciando conta vogais!')
            conta_vogal()
    soma = 0
    consoantes = ''
    j = 0
    while j < len(palavra):
        if palavra[j] not in 'aeiou':
            consoantes += palavra[j]
            soma += 1
        j += 1
        return soma
    
