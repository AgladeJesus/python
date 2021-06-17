sal = float(input('Salário: '))
perc_aum = float(input('Percentual de aumento: '))
aum = sal * ((perc_aum/100)+1)

print('O novo Salário será: R${:.2f}'.format(aum))