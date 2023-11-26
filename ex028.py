# Adivinhe um número entre 0 e 5.

import random
import time
time.sleep(0.5)
print("-=-" * 15)
print(' ' * 6 + "Adivinhe um número entre 0 e 5.")
print("-=-" * 15)

num = int(input("Qual número eu pensei: "))
pc = random.randint(0,5)
time.sleep(1)
if num == pc:
    print(f"O teu número foi {num} e o meu número foi {pc}")
    print(f'Voce acertou!!!')
else:
    print(f"O teu número foi {num} e o meu número foi {pc}")
    print(f"Você errou!")