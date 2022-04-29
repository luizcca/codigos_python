arq = open(r"d:\python\alice.txt")
texto = arq.read()
texto = texto.lower()
import string
for c in string.punctuation:
    texto = texto.replace(c, '')
texto = texto.split()

dic = {}
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1
print('Alice aparece %s vezes' %dic['alice'])
arq.close()
