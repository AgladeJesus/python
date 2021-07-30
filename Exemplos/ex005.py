print('='*20)
print('{:^20}'.format('SACOLA SDL'))
print('='*20)

def tipo_sacola():
        print('''
        [ 0] SAIR DESSE MODULO.
        \033[31m=========PEQUENA=========\033[m
        [ 1] SL PEQ PRETA SDL
        [ 2] SL PEQ ROSA SDL
        [ 3] SL PEQ TIFANY SDL
        [ 4] SL PEQ BRANCA SDL
        \033[31m=========MÉDIA=========\033[m
        [ 5] SL MED PRETA SDL
        [ 6] SL MED ROSA SDL
        [ 7] SL MED TIFANY SDL
        [ 8] SL MED BRANCA SDL
        \033[31m=========GRANDE=========\033[m
        [ 9] SL GRA PRETA SDL
        [10] SL GRA ROSA SDL
        [11] SL GRA  TIFANY SDL
        [12] SL GRA BRANCA SDL
        \033[31m=========MICRO=========\033[m
        [13] SL MICRO PRETA SDL
        [14] SL MICRO ROSA SDL
        [15] SL MICRO  TIFANY SDL
        [16] SL MICRO BRANCA SDL
        \033[31m=========NANO=========\033[m
        [17] SL NANO PRETA SDL
        [18] SL NANO ROSA SDL
        [19] SL NANO  TIFANY SDL
        [20] SL NANO BRANCA SDL
        ''')

PQ = 5.75
MD = 4.55
GR = 13.75
MC = 2.40
NN = 1.8
pct = 100

qtdTotal = 0
qtde = 0
pallet = 0

tipo_sacola()
print('='*40)
print('{:^40}'.format('SOLICITAÇÃO PARA FATURAMENTO'))
print('='*40)
cliente = str(input('Nome da Loja: '))
print('='*25)

while True:
    tipo = int(input('Qual modelo de Sacola: '))
    if tipo == 0:
        break
    elif tipo == 1:
        lanç = int(input('São quantas OS´s para esse pallet: '))
        print('SL PEQ PRETA SDL')
        totalPedido = 0
        cont = 0
        while cont < lanç:
            os = int(input('Nº OS: '))
            qtde = int(input('Qtde de sacola: '))
            totalPedido += qtde
            cont += 1

        if totalPedido <= 6000:
            if lanç == 1:
                # QTDE IGUAL E ABAIXO DE 6000 P/ 1 PALLET, PARA UMA O.S ÚNICA.
                print(f'Qtde de pacotes: {totalPedido / pct :.0f}')
                print('\n')
            else:
                # QTDE IGUAL E ABAIXO DE 6000 P/ 1 PALLET, PARA DUAS O.S DISTINTAS.
                print(f'Qtde de sacolas: {totalPedido :.0f}')
                print(f'Qtde de pacotes: {totalPedido / pct :.0f}')
                print('\n')
        else:
            if lanç == 1:
                # QTDE ACIMA DE 6000 P/ 2 PALLETS, PARA UMA O.S ÚNICA.
                if (totalPedido / pct) % 2 == 0:
                    print('='*20)
                    print('{:^20}'.format('PRIMEIRO PALLET'))
                    print('=' * 20)
                    print(f'Qtde de sacolas: {totalPedido/2 :.0f}')
                    print(f'Qtde de pacotes: {(totalPedido/2)/pct :.0f}')
                    print('\n')

                    print('='*20)
                    print('{:^20}'.format('SEGUNDO PALLET'))
                    print('=' * 20)
                    print(f'Qtde de sacolas: {totalPedido / 2 :.0f}')
                    print(f'Qtde de pacotes: {(totalPedido / 2) / pct :.0f}')
                    print('\n')

                elif (totalPedido / pct) % 2 == 1:
                    print('=' * 20)
                    print('{:^20}'.format('PRIMEIRO PALLET'))
                    print('=' * 20)
                    print(f'Qtde de sacolas: {(totalPedido-pct)/2 :.0f}')
                    print(f'Qtde de pacotes: {((totalPedido-pct)/2)/pct :.0f}')
                    print('\n')

                    print('=' * 20)
                    print('{:^20}'.format('SEGUNDO PALLET'))
                    print('=' * 20)
                    print(f'Qtde de sacolas: {((totalPedido - pct)/2)+pct :.0f}')
                    print(f'Qtde de pacotes: {(((totalPedido - pct)/2)+pct) / pct :.0f}')
                    print('\n')

            else:
                # QTDE ACIMA DE 6000 P/ 2 PALLETS, PARA DUAS O.S DISTINTAS.
                print(f'Qtde de sacolas: {totalPedido}')
                if (totalPedido / pct) % 2 == 0:
                    print('='*20)
                    print('{:^20}'.format('PRIMEIRO PALLET'))
                    print('=' * 20)
                    print(f'Qtde de sacolas: {totalPedido/2 :.0f}')
                    print(f'Qtde de pacotes: {(totalPedido/2)/pct :.0f}')
                    print('\n')

                    print('='*20)
                    print('{:^20}'.format('SEGUNDO PALLET'))
                    print('=' * 20)
                    print(f'Qtde de sacolas: {totalPedido / 2 :.0f}')
                    print(f'Qtde de pacotes: {(totalPedido / 2) / pct :.0f}')
                    print('\n')

                elif (totalPedido / pct) % 2 == 1:
                    print('=' * 20)
                    print('{:^20}'.format('PRIMEIRO PALLET'))
                    print('=' * 20)
                    print(f'Qtde de sacolas: {(totalPedido-pct)/2 :.0f}')
                    print(f'Qtde de pacotes: {((totalPedido-pct)/2)/pct :.0f}')
                    print('\n')

                    print('=' * 20)
                    print('{:^20}'.format('SEGUNDO PALLET'))
                    print('=' * 20)
                    print(f'Qtde de sacolas: {((totalPedido - pct)/2)+pct :.0f}')
                    print(f'Qtde de pacotes: {(((totalPedido - pct)/2)+pct) / pct :.0f}')
                    print('\n')


    qtdTotal += qtde

print(f'Quatidade total de sacolas: {qtdTotal}')