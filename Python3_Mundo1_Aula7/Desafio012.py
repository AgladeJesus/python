pr = float(input('Valor do Produto: R$ '))
des = pr * (5/100)
res = pr - des

print('Valor do produto: R${}'.format(pr))
print('Valor do desconto de 5%: R${}'.format(des))
print('Valor do produto com desconto: R${}'.format(res))
