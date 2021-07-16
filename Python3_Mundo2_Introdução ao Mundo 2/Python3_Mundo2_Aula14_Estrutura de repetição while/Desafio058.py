from random import randint
from time import sleep
rdpc = randint(1, 10)
nm = 0
cont = 0
print('-=-' * 20)
print('Vou pensar em um número entre 1 e 10. Tente descobrir...')
print('-=-' * 20)
print(rdpc)
while nm != rdpc:
    nm = int(input('Em qual número eu pensei? '))
    print('PROCESSANDO...')
    sleep(0.3)
    cont += 1
    if nm == rdpc:
        print('PARABÉNS, VOCÊ ACETOU!')
        print('Você precisou de {} tentativas'.format(cont))
    else:
        print('GANHEI! O número que eu pensei foi {} e não o {}'.format(rdpc, nm))

