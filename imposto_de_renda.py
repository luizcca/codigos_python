print("\n\nINSERI DOIS VALORES E VERIFICA QUAL O MAIOR VALOR DIGITADO")
nome = input("Digite o seu nome: ")
salario = float(input("Digite o salario: "))
faixa1 = 0.12
faixa2 = 0.19
faixa3 = 0.27

if salario < 1000:
    print ("Você é isento de pagar IR")
elif salario < 3000:
    imposto = salario * faixa1
    print ("Você desconta R$",imposto," de seu salario, logo seu salario liquido é: ",salario - imposto)
elif salario < 5000:
    imposto = salario * faixa2
    print ("Você desconta R$",imposto," de seu salario, logo seu salario liquido é: ",salario - imposto)
elif salario > 5000:
    imposto = salario * faixa3
    print ("Você desconta ",imposto," de seu salario, logo seu salario liquido é: ",salario - imposto)
