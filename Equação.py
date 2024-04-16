num1 = int(input("insira um numero"))
num2 = int(input("insira o segundo numero"))
num3 = int(input("insira o terceiro numero"))

if num1 > num2 and num1 > num3:
    print("o numero maior é %.1f" %(num1))
elif num2 > num1 and num2 > num3:
    print("o numero maior é %.1f" %(num2))
elif num3 > num1 and num3 > num2:
    print("O numero maior é %.1f" %(num3))
else:
    print("Numero invalido")
if num1 < num2 and num1 < num3:
    print(f"o {num1} é o menor")
elif num2 < num1 and num2 < num3:
    print(f"o {num2} é o menor")
elif num3 < num1 and num3 < num2:
    print(f"o {num3} é o menor")

