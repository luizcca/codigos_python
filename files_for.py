ref_arquivo = open("qbdata.txt","r")

for linha in ref_arquivo:
    valores = linha.split()
    print('QB ', valores[0], valores[1], 'obteve a avaliacao ', valores[10] )


ref_arquivo.close()

#First Name, Last Name, Position, Team, Completions, Attempts, Yards, TDs Ints, Comp%, Rating
