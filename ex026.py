# Analizando profundamente a frase

text = input("Digite a frase: ")
text.strip().lower()

print(f'A letra "A" aparece {text.count("a")} vezes')
print(f'A primeira letra "A" apareceu na posição {text.find("a")+1}')
print(f'A última letra "A" apareceu na posição {text.rfind("a") + 1}')