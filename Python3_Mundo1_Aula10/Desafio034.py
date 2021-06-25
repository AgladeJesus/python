sal = float(input('Qual o salário do funcionário: '))

perc10 = sal * ((10/100) + 1)
perc15 = sal * ((15/100) + 1)

if sal <= 1250.00:
    print('O salário ajustado é: R${}'.format(perc15))
else:
    print('O salário ajustado é: R${}'.format(perc10))

