letra = (input("Inisira sua letra "))

vogais = { "a", "e", "i", "o", "u"}

consoantes = {"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "y", "w", "z"}

if letra.lower() in vogais:
    print("a letra é vogal")

elif letra.lower() in consoantes:
    print("a letra é consoante")
else:
    print("Caractere invalido, inisra outro")

