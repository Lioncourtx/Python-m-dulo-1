# Desconto em produto de 5%

valor = float(input("Digite o valor do produto: "))
desc = valor - (valor * 0.05)

print(f"Esse produto com o desconto de 5% custará R${desc:.2f}")