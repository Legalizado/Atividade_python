import math

valor = float(input("Qual o valor que voce quer calcular a raiz quadrada? "))
    
if valor > 1 :
    valor = math.sqrt(valor)
    print(valor)  
else:
    print("valor invalido, insira um numero positivo em cima")



