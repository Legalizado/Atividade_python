temperatura = input("Qual a temperatura, Celcius, ou Fahrenheit? ")
valor = float(input("Inspira a temperatura atural? "))

if temperatura == "c" or temperatura.lower() == "celcius":
    celcius = (valor * 1.8) + 32
    print("A sua temperatura em Celcius é ", celcius)
elif temperatura == "f" or temperatura.lower() == "fahrenheit":
    fahren = (valor - 32) / 1.8 
    print("Sua temperatura em Fahrenheit é ", fahren)

