a = int(input('Construa a tabuada do Número: '))

aux = 0

print('*' * 18)
print('Trabuada de {}'.format(a))
print('*' * 18)

for aux in range(1, 11):
    print('{} + {:2} = {:4}  === | === {} - {:2} = {:4} === | === {} X {:2} = {:4}  === | === {} / {:2} = {:.2f}'.format(a, aux, (a + aux), a, aux, (a - aux), a, aux, (a * aux), a, aux, (a / aux)))
    aux = aux + 1