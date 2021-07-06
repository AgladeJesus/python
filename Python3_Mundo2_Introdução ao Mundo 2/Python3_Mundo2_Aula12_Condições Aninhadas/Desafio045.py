print('-='*20)
print('JOGO DE PEDRA, PAPEL OU TESOURA (JAKENPÔ)')
print('-='*20)

print('PEDRA')
print('PAPEL')
print('TESOURA\n\n')

jgd1 = str(input('Jogador 1: '))
jgd2 = str(input('Jogador 2: '))

print('Jogador 1 escolheu: {}'.format(jgd1))
print('Jogador 2 escolheu: {}'.format(jgd2))

if (jgd1 == 'PEDRA' and jgd2 == 'TESOURA') or (jgd1 == 'PAPEL' and jgd2 == 'PEDRA') or (jgd1 == 'TESOURA' and jgd2 == 'PAPEL'):
    print('Parabéns jogador 1, você ganhou!')
else:
    print('Parabéns jogador 2, você ganhou!')





