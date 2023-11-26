# Descobrindo a Hipotenuza
import math

co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))
h = math.hypot(ca, co)
print((f"A hipotenuza dos catetos {co} e {ca} é igual a {h:.2f}"))