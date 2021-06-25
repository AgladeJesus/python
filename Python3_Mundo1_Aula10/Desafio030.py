nm = int(input('Digite um número: '))

pi = nm % 2

if pi == 0:
    print('O número {}, que você digitou é: PAR'.format(nm))
else:
    print('O número {}, que você digitou é: ÍMPAR'.format(nm))