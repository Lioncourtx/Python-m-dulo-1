# Calculando o valor da viagem

travel = float(input("Digite o a quilometragem da viagem: "))

if travel <= 200:
    print(f"Tua viagem é de {travel}km")
    print(f"O valor da viagem ficará em R${travel * 0.50:.2f}")
else:
    print(f"Tua viagem é de {travel}km")
    print(f"O valor da viagem ficará em R${travel * 0.45:.2f}")
