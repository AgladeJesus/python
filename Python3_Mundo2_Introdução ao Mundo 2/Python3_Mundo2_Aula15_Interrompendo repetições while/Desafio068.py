from random import randint

print('Olá, caro jogador, sou o computador, e quero dispultar com você no Impar/Par.')

while True:
    jogador = int(input('Digita um número de 1 a 10: '))
    cp = randint(0, 10)
    total = jogador + cp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ìmpar: [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {cp}, o total é {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!')
        else:
            print('Você PERDEU!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!!')
        else:
            print('Você PERDEU!!')
            break
print('Vamos jogar novamente...')

