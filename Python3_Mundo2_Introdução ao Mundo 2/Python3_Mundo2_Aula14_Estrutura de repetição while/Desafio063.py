from time import sleep
print('-='*20)
print('SEQUÊNCIA DE FIBONACCI')
print('-='*20)
n = int(input('Quantos termos você quer mostrar? '))
nm1 = 0
nm2 = 1
print('~'*20)
print('{} -> {}'.format(nm1, nm2), end='')
cont = 3
while cont <= n:
    nm3 = nm1 + nm2
    print(' -> {}'.format(nm3), end='')
    nm1 = nm2
    nm2 = nm3
    cont += 1
    sleep(0.3)
