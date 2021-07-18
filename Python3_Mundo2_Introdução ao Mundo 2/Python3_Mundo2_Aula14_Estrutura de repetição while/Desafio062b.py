print('-='*20)
print('PROGRESSÃO ARITMÉTICA')
print('-='*20)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(primeiro), end='')
        primeiro += razão
        cont += 1
    print('PAUSA!')
    mais = int(input('Quantos trmos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(cont))
print('FIM!')