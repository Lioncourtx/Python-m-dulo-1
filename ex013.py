salario  = float(input("Digite o salario: "))
aumento = int(input("Digite o aumento em %: "))

novoSalario = salario + ((aumento / salario ) * 100)

print(f"o salario de R${salario:.2f}, com aumento de {aumento}%, será de R${novoSalario:.2f}")