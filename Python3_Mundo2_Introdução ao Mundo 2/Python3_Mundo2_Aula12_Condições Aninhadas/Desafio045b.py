from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
sleep(0.2)
print('-='*15)
print('O Computador jogou {}'.format(itens[pc]))
print('O Jogador jogou {}'.format(itens[jogador]))
print('-='*15)

if pc == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('EU VENCI')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU!')
elif pc == 1:
    if jogador == 0:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('EU VENCI')
elif pc == 2:
    if jogador == 0:
        print('EU VENCI')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE')
