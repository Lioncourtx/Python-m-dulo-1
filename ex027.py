# Analisando nomes

name = str(input("Digite o teu nome todo: ")).title().strip()

print(f"Prazer em conhecer você {name.split()[0]}!")
print(f"Teu primeiro nome é : {name.split()[0]}!")
print(f"Teu último nome é : {name.split()[-1]}!")