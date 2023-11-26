# Analisando ano Bissexto

from datetime import date
ano = int(input("Digite qual ano você quer analisar (Coloque 0 para o ano atual): "))

year = int(date.today().year)

if ano == 0:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"O ano {year} é bissexto")
    else:
        print(f"O ano {year} não é bissexto")
else:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f"O ano {ano} é bissexto")
    else:
        print(f"O ano {ano} não é bissexto")