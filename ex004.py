# Análise de dados
text = input("Digite algo: ")
print(f"{text} é texto ? {text.isalpha()}")
print(f"{text} é número ? {text.isalnum()}")
print(f"{text} está tudo em maiusculo ? {text.isupper()}")
print(f"{text} está tudo em minuscula ? {text.islower()}")
print(f"{text} tem espaço ? {text.isspace()}")
print(f"{text} está com a primeira letra maiuscula ? {text.istitle()}")