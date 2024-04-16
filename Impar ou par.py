numero = input("Qual o numero que você deseja realizar a tabuada?")


c = 0 

while c < 10:
    c = c + 1 
    resultado = int(c) * int(numero)
    print("{} x {} = {}" .format(numero, c, resultado))
    
    
    
