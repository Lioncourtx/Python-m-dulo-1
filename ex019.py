# Sorteio entre alunos

import random

n1 = input("Digite o nome do primeiro Aluno: ")
n2 = input("Digite o nome do segundo Aluno: ")
n3 = input("Digite o nome do terceiro Aluno: ")
n4 = input("Digite o nome do quarto Aluno: ")
pick = random.choice([n1, n2, n3, n4])

print(f"O nome do aluno(a) escolhido foi {pick}")