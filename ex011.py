# Tinta para Parede

h = float(input("Digite a altura da parede: "))
l = float(input("Digite a largura da parede: "))
wall = h * l
lata = wall / 2

print(f"Uma parede com {h}m x {l}m tem {wall}m²")
print(f"Para pintar essa parede é necessário {lata:.3f}l de tinta.")