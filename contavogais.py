def contaVogais(palavras):
    vogal = []
    """return the number of vowels appearing in word
    (by default, the string of vowels is ’aeiouy’)"""
    vogais = 'aeiou'
    ocorrencias = [c for c in palavra.lower() if c in vogais]
    return len(ocorrencias)


palavra = input("Insira uma frase longa: ")
print("Existem {} vogais na frase.".format(contaVogais(palavra)))
