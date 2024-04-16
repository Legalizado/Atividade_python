import math

print("insira os valores para a equação a ax2 + bx + c")

a = float(input("Insira o valor de A: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de b: "))

d = b**2 - 4 * a * c

if (a == 0):
    exit(print("0 é um numero invalido, a equação não é do segundo grau"))

if (d <0):
    exit(print("a equação não possui raizes reais"))
elif(d == 0):
    print("A equação só possui uma raiz real")
elif(d >0):
   print("o valor de delta é %.2f" %(d))
r1 = (-b - math.sqrt(d)) / (2 * a)
r2 = (-b + math.sqrt(d)) / (2 * a)

print("A raiz 1 e é %.2f,a raiz2 é %.2f" %(r1, r2))
 



