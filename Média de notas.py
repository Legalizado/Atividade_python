nota = float(input("Qual o valor da nota do aluno? "))

if nota > 86 and nota < 100:
    print("A")
elif nota > 61 and nota < 85:
    print("B")

elif nota > 36 and nota < 60:
    print("C")
elif nota > 35 and nota < 1:
    print("D")
elif nota == 0:
    print("E")
else:
    print("Caractere invalido")
