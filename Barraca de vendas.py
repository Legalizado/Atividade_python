catalogo = {
        "100": 1.20,
        "101": 1.30,
        "102": 1.50,
        "103": 1.20,
        "104": 1.70,
        "105": 2.20,
        "106": 1.10
    }
    
  
    
codigo = (input("Qual o codigo do produto? "))
quantidade = (input("Quantas unidades voce quer? "))

if codigo in catalogo:
    preco = catalogo[codigo]
    total = float(preco) * float(quantidade)
    print(total)
else:
    print("ta de maracutaia")
