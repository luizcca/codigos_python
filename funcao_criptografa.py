def esconde(msg):
    s = ''
    for a in msg:
        s += chr(ord(a) + 10000)
    return s

def mostra(msg):
    s = ''
    for c in msg:
        s += chr(ord(c) - 10000)
    return s


