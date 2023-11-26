# Aluguel de carro

aluguel = int(input("Digite a quantidade de dias: "))
km = int(input("Digite a quilometragem: "))

valorAluguel = aluguel * 60
valorKm = km * 0.15
total = valorAluguel + valorKm

print(f"O Valor total do carro ficou em R${total:.2f}")