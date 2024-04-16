login = input("Insira seu nome de usuario ")
senha = input("Insira sua senha ")

if login.lower() == "userpy" and senha == "Teste123":
    print("Login efetuado")
else:
    print("usuario ou senha invalidos")
