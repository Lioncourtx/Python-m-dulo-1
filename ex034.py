# Cálculo de Aumento de salário.

salario = float(input("Digite o salário: "))

if salario > 1250:
    print(f"O salário de R${salario:.2f} terá um aumento de 10% para R${salario * 1.10:.2f}")
else:
    print(f"O salário de R${salario:.2f} terá um aumento de 15% para R${salario * 1.15:.2f}")