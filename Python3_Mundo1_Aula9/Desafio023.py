nm = int(input('Digite um número: '))
u = nm // 1 % 10
d = nm // 10 % 10
c = nm // 100 % 10
m = nm // 1000 % 10
print('Analisando o número {}'.format(nm))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))