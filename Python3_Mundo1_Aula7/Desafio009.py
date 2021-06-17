a = int(input('Construa a tabuada do Número: '))

aux = 0

print('*' * 18)
print('Trabuada de {}'.format(a))
print('*' * 18)

while (aux <= 10):
    print('{} X {} = {}'.format(a, aux, (a * aux)))
    aux = aux + 1
