n1 = int(input('um Valor: '))
n2 = int(input('Outro Valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
sb = n1 - n2
rest = n1 % n2
print('A soma é: {}, a multiplicação é: {}, a divisão é: {:.3f}'.format(s,m,d), end=' ')
print('Divisão inteira é: {}, a Esponeciação é: {}, a Subtração é: {}, e o resto da divisão é: {}'.format(di,e,sb,rest))