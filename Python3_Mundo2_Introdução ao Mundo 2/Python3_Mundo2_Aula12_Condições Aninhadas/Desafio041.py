from datetime import date
anoNasc = int(input('Ano de nascimento'))

anoAtual = date.today().year

idade = anoAtual-anoNasc

if idade <= 9:
    print('MIRIM')
elif idade 