pr = float(input('Valor do Produto: R$ '))
novo = pr - (pr * (5/100))

print('Valor do produto: R${}'.format(pr))
print('Valor do desconto de 5%: R${}'.format(pr * (5/100)))
print('Valor do produto com desconto: R${}'.format(novo))
