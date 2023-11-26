# Radar de velocidade de um carro.

speed = float(input("Qual é a velocidade atual do carro? "))

if speed <= 80:
    print(f"Tua velocidade é de {speed}Km/h")
else:
    print(f"Tua velocidade é de {speed}km/h")
    print(f"Você foi multado em R${(speed - 80) * 7:.2f}")

print("Dirija com segurança!")