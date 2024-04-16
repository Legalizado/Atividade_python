numero = int(input("Qual o numero voce quer? "))

if numero < 0:
    print("numero invalido, insira um numero postivo")
else:  
    if numero % 2 == 0:
        print("Este numero é par")
    elif numero % 2 != 0:
         print("Este numero e impar")



