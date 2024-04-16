num1 = float(input("insira seu primeiro numero "))
num2 = float(input("insira seu segundo numero "))

oper = input("Qual operação voce deseja?\n +(adição) \n -(subtração) \n *(vezes) \n / (divisão)?\n ")

if oper.lower() == "+" or oper.lower() == "adição":
    res = num1 + num2
    print(res)
elif oper.lower() == "-" or oper.lower() == "subtração":
    res = num1 - num2
    print(res)
elif oper.lower() == "*" or oper.lower() == "vezes":
    res = num1 * num2
    print(res)
elif oper.lower() == "/" or oper.lower() == "divisão":
    res = num1 / num2
    print(res)
else:
    ("Numero invalido")
