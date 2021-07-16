print('-='*20)
print('PROGRESSÃO ARITMÉTICA')
print('-='*20)

termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
dez = termo + (20 -1 ) * razão
for c in range(termo, dez + razão, razão):
    print('{}'.format(c), end='-> ')
print('ACABOU!')