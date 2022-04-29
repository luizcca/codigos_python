#FUNCAO PARA EMBARALHAR AS LETRAS DE UMA PALAVRA DADA

def embaralha(s):
    import random
    lista = list(s)
    random.shuffle(lista)
    return ''.join(lista)

"""
#ENTRADA DE DADOS E SAIDA EM VIDEO
>>> embaralha('canonical')
'lacnacino'
>>> embaralha('canonical')
'aiacclnno'
>>> embaralha('canonical')
'nlanoacci'
>>> embaralha('canonical')
'nicacaonl'
"""
