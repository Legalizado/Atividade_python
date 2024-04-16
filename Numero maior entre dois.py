
numero_1 = float(input("Insira o primeiro numero "))
numero_2 = float(input("Insira o segundo numero "))
 
if numero_1 > numero_2 :
    res1 = "o {:.1f} é o maior numero"  .format(numero_1)
    print(res1)
elif numero_1 < numero_2:
     res2 = "o %.1f é o maior numero" % numero_2
     print(res2)
elif numero_1 == numero_2:
     print("Numeros iguais")
