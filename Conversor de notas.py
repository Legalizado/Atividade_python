
print('Qual é o valor das notas?')
nota1 = float(input("nota1: "))
nota2 = float(input("nota2: "))
 
 

 
soma = float(nota1) + float(nota2)
media = soma / 2
print(float(media))


if (media>10):
    print("Numero invalido, limite de nota 10")
elif (media>=7):
    print("aprovado")
elif (media<7) and (media>=5):
    print("recuperação")
elif (media<5):
    print("reprovado")

    

 
