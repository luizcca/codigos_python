listaLigada = [["Francis","English", 435],
               ["Larry", "Maths", 234],
               ["Nicole", "Biology", 986],
               ["Joey", "Physics", 562],
               ["Sam", "Computing", 12],]

print(": Primeiro nome : Disciplina : pontuação :")

for item in listaLigada:
    print("|", item[0]," "*(9-len(item[0])),"|",
          item[1]," "*(19-len(item[1])),"|",
          item[2]," "*(4-len(str(item[2]))),"|")
