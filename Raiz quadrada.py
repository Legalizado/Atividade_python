calendario = {
    "1": "Janeiro",
    "2": "Fevereiro",
    "3": "Março",
    "4": "Abril",
    "5": "Maio",
    "6": "Junho",
    "7": "Julho",
    "8": "Agosto",
    "9": "Setembro",
    "10": "Outubro",
    "11": "Novembro",
    "12": "Dezembro"
}

mes = input("Qual o mumero do mes? ")

if mes in calendario:
    nome = calendario[mes]
    print(nome)
else:
    print("ta de maracutaia, nao existe esse mes...")

