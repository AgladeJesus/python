a = int(input('Construa a tabuada do Número: '))

aux = 0

print('*' * 18)
print('Trabuada de {}'.format(a))
print('*' * 18)

for aux in range(1, 10):
    print('{} X {:2} = {:4}'.format(a, aux, (a * aux)))
    aux = aux + 1