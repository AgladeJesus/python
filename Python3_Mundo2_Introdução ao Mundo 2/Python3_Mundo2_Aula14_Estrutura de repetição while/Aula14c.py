r = 'S'
c = 0
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
    c = c +1
print('Houve {} repetições.'.format(c-1))
print('Fim')