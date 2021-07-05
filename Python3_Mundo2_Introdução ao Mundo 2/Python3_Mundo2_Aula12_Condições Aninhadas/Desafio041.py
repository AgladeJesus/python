from datetime import date
anoNasc = int(input('Ano de nascimento: '))

anoAtual = date.today().year

idade = anoAtual-anoNasc

if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JUNIOR')
elif idade > 19 and idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
    