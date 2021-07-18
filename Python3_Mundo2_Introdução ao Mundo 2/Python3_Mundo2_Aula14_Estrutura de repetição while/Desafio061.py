'''print('-='*20)
print('PROGRESSÃO ARITMÉTICA')
print('-='*20)

termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
dez = termo + (20 -1 ) * razão
for c in range(termo, dez + razão, razão):
    print('{}'.format(c), end='-> ')
print('ACABOU!')'''

print('-='*20)
print('PROGRESSÃO ARITMÉTICA')
print('-='*20)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM!')

print('\n\n')

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 1
while cont <= 10:
    print('{} -> '.format(primeiro), end='')
    primeiro += razão
    cont += 1
print('FIM!')