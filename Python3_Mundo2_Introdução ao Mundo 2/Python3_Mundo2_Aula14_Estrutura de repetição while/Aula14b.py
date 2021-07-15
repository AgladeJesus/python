'''for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')'''

n = 1
c = 0
while n != 0:
    n = int(input('Digite um valor: '))
    c += 1
print('Houve {} repetições.'.format(c-1))
print('Fim')