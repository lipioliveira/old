nomeCompleto = str(input("Digite seu nome completo:")).strip()
print("Analisando seu nome...")
print("Seu nome em maiúsculo é {}".format(nomeCompleto.upper()))
print("Seu nome em minúsculo é {}".format(nomeCompleto.lower()))
print("Seu nome tem {} letras".format(len(nomeCompleto)-(nomeCompleto.count(" "))))
print("Seu primeiro nome tem {} letras".format(nomeCompleto.find(" ")))