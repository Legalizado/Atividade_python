num = input("insira o seu mes ")

d30 = {"abril", "4",
    "junho", "6",
    "setembro", "9",
    "novembro", "11"}

d31 = {    "janeiro", "1",
    "março", "3",
    "maio", "5",
    "julho", "7",
    "agosto", "8",
    "outubro", "10",
    "dezembro", "12"}
    



if num == "2" or num == "fevereiro":
    print("28 dias")
elif num.lower() in d30:
    print("30 dias")
elif num.lower() in d31:
    print("31 dias")
else:
    print("Numero invalido")

