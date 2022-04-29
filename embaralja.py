def embaralha(txt):
    import random
    lista = list(txt)
    random.shuffle(lista)
    return ''.join(lista)
