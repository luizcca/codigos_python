import pprint
texto = "Eu sou o rei em minha casa!"
contador = []
for char in texto:
    contador.setdefault(char, 0)
    contador[char] += 1
pprint.pprint(contador)
