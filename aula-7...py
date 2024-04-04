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
