#Entrada de dados via teclado
# https://www.youtube.com/watch?v=f4Uuwdhy-OA&index=7&list=PL2QkKoTK1V5Hslg25Id85OoOQRBlQsHcJ

print("INSERIR IDADE DO USUARIO:")
idade = int(input("Digite a sua idade: "))
print("A sua idade é: ",idade)

print("\n\nINSERI QUANTIDADE DE HORAS TRABALHADAS E RETORNA VALOR A RECEBER PELO PROGRAMADOR:")
if idade > 40 and idade % 2 == 0:
    horas_trabalhadas = int(input ("Insira a quantidade de horas trab: "))
    valor_hora_trab = horas_trabalhadas * 50
    print("Você tem direito a receber: R$ ",valor_hora_trab," pelas ",horas_trabalhadas,"horas trabalhadas")
    print("e a sua idade ",idade," é par")
else:
    print("Trabalhe duro e você receberá um pagamento.")
    


print("\n\nINSERI A TEMPERATURA EM FERHEING E RETORNA VALOR DA TEMPERATURA EM CELSIUS")
f = int(input("Digite a temperatura em f: "))
celsius = 5 * (f - 32)/9
print("A temperatura em celsius equivalente a ",f,"f é: ",celsius)


print("\n\nINSERI DOIS VALORES E VERIFICA QUAL O MAIOR VALOR DIGITADO")
x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o primeiro valor: "))
if x > y:
    print (x, "é o mair valor digitado")
elif x < y:
    print (y, "é o maior valor digitado")
else:
    print ("Os valores digitados são iguais a: ", x)


print("\n\nINSERI NOME E NOTAS DE UM ALUNO E CALCULA SUA MEDIA")

nome = input("Digite seu nome: ")
nota1 = float(input("Digite nota1: "))
nota2 = float(input("Digite nota2: "))
nota3 = float(input("Digite nota2: "))
media = (nota1 + nota2 + nota3) / 3.0
if media >= 5:
    print ("O aluno ",nome,"foi aprovado com a media",media)
else:
    print ("O aluno ",nome,"foi reprovado, pois sua media foi ",media)
