# Analisador de texto
nome = input("Digite o teu nome completo: ")

print(f"Teu nome em MAIUSCULO é: {nome.upper()}")
print(f"Teu nome em minusculo é: {nome.lower()}")
print(f"Teu nome ao todo tem  {len(nome)} letras")
print(f"Teu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras")