from random import randint
from time import sleep

rdpc = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente descobrir...')
print('-=-' * 20)
nm = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(2)

if nm == rdpc:
    print('PARABÉNS, VOCÊ ACETOU!')
else:
    print('GANHEI! O número que eu pensei foi {} e não o {}'.format(rdpc, nm))