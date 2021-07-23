from random import randint

print('Olá, caro jogador, sou o computador, e quero dispultar com você no Impar/Par.')
v = 0
while True:
    jogador = int(input('Digita um número de 1 a 10: '))
    cp = randint(0, 10)
    total = jogador + cp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ìmpar: [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {cp}, o total é {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!')
            v += 1
        else:
            print('Você PERDEU!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!!')
            v += 1
        else:
            print('Você PERDEU!!')
            break
if v > 0:
    print(f'Você tem {v} votórias')
else:
    print(' ')
print('Vamos jogar novamente...')

