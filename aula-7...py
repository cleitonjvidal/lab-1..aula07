#Crie um programa que leia o nome, o salário e o tempo de serviço de um funcionário e informe se ele tem direito a receber um aumento. 
#O funcionário deve ter pelo menos 5 anos de serviço e o salário não pode ser superior a R$ 2.000,00 para receber o aumento de 10%. 
#Caso contrário, o aumento é de 5%.


nome = input("digite seu nome: ")
salario = float(input("digite seu salario: "))
tempoDEservico = float(input("digite os anos trabalhadas:"))



if tempoDEservico >=5 and salario <= 2000: 
    aumento = salario * 0.10

else:
    aumento = salario * 0.05

novosalario = salario + aumento    

print(f"o funcionario {nome} recebera um aumento de {aumento :2}" )  
print("novo salario sera de R$:" ,novosalario )







#Faça um script que peça os 3 lados de um triângulo. O script deverá informar se os valores podem ser um triângulo. 
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;


ladoUM = float(input("digite o valor do primeiro lado: "))
ladoDOIS = float(input("digite o valor do segundo lado:"))
ladoTRES = float(input("digite o valor do terceiro lado"))

if ladoUM == ladoDOIS and ladoUM == ladoTRES: 
    print("triangulo equilatero")

elif ladoUM == ladoDOIS or ladoUM == ladoTRES or ladoDOIS == ladoTRES:
    print("triangulo isosceles:")

else:
    print("triangulo escaleno:")




#Faça um algoritmo que leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
#Também solicite qual a % de frequência e aula, verifique e apresente a seguinte mensagem:
#Aprovado: Nota maior ou igual a 7,0 e frequência igual ou superior a 75%.
#Exame: Nota maior ou igual a 4,0 e menor que 7,0 e frequência superior a 75%.
#Reprovado: Nota inferior a 4,0 ou frequência menor que 75%.



notaUm = float(input("digite a primeira nota: "))
notaDOIS = float(input("digite a segunda nota: "))
frequencia = float(input("digite a sua frequencia: "))

media = (notaUm + notaDOIS) / 2

if media >= 7 and frequencia >=75: 
    print(f"sua media é {media} esta aprovado ")

elif media >=4  and frequencia >=75: 
    print(f"sua media é {media} esta no exame: ")

elif media <=3 and frequencia >=75:
    print(f"sua media e {media} reprovado")

else:
    print("reprovado")




    print("responda sim ou não para cada pergunta! ")

perguntaUM = input("telefonou para a vitima?")
perguntaDOIS = input("esteve no local do crime?")
perguntaTRES = input("morava perto da vitima?")
perguntaQUATRO =input("devia para a vitima?")
perguntaCINCO = input("ja trabalhou com a vitima?")

respostasPOSITIVAS = 0


if perguntaUM == "sim":
    respostasPOSITIVAS += 1
if perguntaDOIS == "sim":
    respostasPOSITIVAS += 1
if perguntaTRES == "sim":
    respostasPOSITIVAS += 1
if perguntaQUATRO == "sim":
    respostasPOSITIVAS += 1
if perguntaCINCO == "sim":
    respostasPOSITIVAS+= 1

if respostasPOSITIVAS == 2:
    print("Classificação: Suspeita")
elif 3 <= respostasPOSITIVAS <= 4:
    print("Classificação: Cúmplice")
elif respostasPOSITIVAS == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")





#Uma fruteira está vendendo frutas com a seguinte tabela de preços:

 #                             Até 5 Kg                 Acima de 5 Kg
 #   Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
  #  Maçã              R$ 1,80 por Kg          R$ 1,50 por Kg

#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e 
#escreva o valor a ser pago pelo cliente.






ate5KGdemorango = 2.50
acima5KGdemorango = 2.20
ate5KGdemaca = 1.80
acima5kgdemaca = 1.50

pesomorangos = float(input("Quantidade de morangos (em Kg): "))
pesomacas = float(input("Quantidade de maçãs (em Kg): "))

if pesomorangos <= 5:
    valormorangos =pesomorangos * ate5KGdemorango
else:
    valormorangos = pesomorangos * acima5KGdemorango

if pesomacas <= 5:
    valormacas = pesomacas * ate5KGdemaca

else:
    valormacas = pesomacas * acima5kgdemaca
    valorfinal = valormorangos + valormacas

    
if pesomorangos + pesomacas > 8 or valorfinal > 25:
    valorfinal *= 0.9

    print(f"voce deve pagar R$ {valorfinal}")










    















    







