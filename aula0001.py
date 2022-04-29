num1,num2 = 40, 30
string1="FELICIDADE"
if num1<num2: #A linha abaixo deverá ser indentada
 print ("O primeiro número informado é {} e é menor que {}. A soma entre elas é {}.".format(num1, num2, num1+num2)) #Perceba a concatenação
else:
 print ("O primeiro número informado é {} e não é menor que {}. A soma entre elas é {}.".format(num1, num2, num1+num2))
print ("O texto informado é {}.".format(string1))

num3 = 90
print (float(num3)) #Esta é uma conversão por casting (inteiro para float)
num4=34.90
print(num4)

f = open('dados.txt', 'r') # abre para leitura ('r'eader)
for line in f:
 print (line[0] + line[1]) #exibe na tela as coluna 0 e 1 (numero da amostra)
 peso = line[3] + line[4] #grava em peso as colunas 3 e 4 (peso)
 altura = line[6] + line[7] + line[8] #grava em altura as colunas 6, 7 e 8 (altura)
 peso = float(peso) #conversão por casting, pois os dados lidos são strings
 altura = float(altura) #conversão por casting, pois os dados lidos são strings
 altura = altura/100 #transformação da altura cm -> mt
 imc = peso / altura**2 #calculo do imc
 print (imc) #exibição do resultado na tela
f.close()
