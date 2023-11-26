# Analisando número entre 0 e 9999

n = int(input("Digite um número entre 0 e 9999: "))

print(f"Analizando o número {n}...")
print(8 * "-=")
print(f"Unidade: {n // 1 % 10}")
print(f"Dezena: {n // 10 % 10}")
print(f"Centena: {n // 100 % 10}")
print(f"Milhar: {n // 1000}")
print(8 * "-=")