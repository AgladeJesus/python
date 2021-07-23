print('-='*10)
print('SACOLA SDL')
print('-='*10)

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

pesoPQ = 5.75
pesoMD = 4.55
pesoGR = 13.75
pesoMC = 2.40
qtdePQ = 100
qtdeMD = 50
qtdeGR = 100
qtdeMC = 100

qtdTotal = 0
qtde = 0

tipo_sacola()
print('-='*25)
print('SOLICITAÇÃO PARA FATURAMENTO')
print('-='*25)
cliente = str(input('Nome da Loja: '))
print('-='*25)
while True:
    tipo = int(input('Qual tipo de Sacola: '))
    if tipo == 0:
        break
    elif tipo == 1:
        lanç = int(input('São quantas OS´s para esse pallet: '))
        print('SL PEQ PRETA SDL')
        totalP = 0
        cont = 0
        while cont < lanç:
            os = int(input('Nº OS: '))
            qtde = int(input('Qtde de sacola: '))
            totalP += qtde
            cont += 1
        if lanç == 1:
            print(f'Qtde de pacotes: {totalP / qtdePQ:.0f}\nPeso: {(totalP / qtdePQ) * pesoPQ:.2f} Kg\nQtde de Alças: {totalP*2} unid. Sendo {totalP/totalP:.0f} pct\nQtde de Fundo: {totalP} unid. Sendo {totalP/1000}\n')
        else:
            print(f'Qtde total: {totalP}\nQtde de pacotes: {totalP / qtdePQ:.0f}\nPeso: {(totalP / qtdePQ) * pesoPQ:.2f} Kg\nQtde de Alças: {totalP*2} unid. Sendo {totalP/totalP:.0f} pct\nQtde de Fundo: {totalP} unid. Sendo {totalP/1000:.0f} pct\n')
    elif tipo == 2:
        print('SL PEQ ROSA SDL')
        os = int(input('Nº OS: '))
        qtde = int(input('Qtde de sacola: '))
        print(f'Qtde de pacotes: {qtde/qtdePQ:.0f}\nPeso: {(qtde/qtdePQ)*pesoPQ} Kg\n')
    elif tipo == 3:
        print('SL PEQ TIFANY SDL')
        os = int(input('Nº OS: '))
        qtde = int(input('Qtde de sacola: '))
        print(f'Qtde de pacotes: {qtde/qtdePQ:.0f}\nPeso: {(qtde/qtdePQ)*pesoPQ} Kg\n')
    elif tipo == 4:
        print('SL PEQ BRANCA SDL')
        os = int(input('Nº OS: '))
        qtde = int(input('Qtde de sacola: '))
        print(f'Qtde de pacotes: {qtde/qtdePQ:.0f}\nPeso: {(qtde/qtdePQ)*pesoPQ} Kg\n')

    elif tipo == 5:
        print('SL MED PRETA SDL')
        os = int(input('Nº OS: '))
        qtde = int(input('Qtde de sacola: '))
        print(f'Qtde de pacotes: {qtde/qtdeMD:.0f}\nPeso: {(qtde/qtdeMD)*pesoMD} Kg\n')
    elif tipo == 6:
        print('SL MED ROSA SDL')
        os = int(input('Nº OS: '))
        qtde = int(input('Qtde de sacola: '))
        print(f'Qtde de pacotes: {qtde/qtdeMD:.0f}\nPeso: {(qtde/qtdeMD)*pesoMD} Kg\n')
    elif tipo == 7:
        print('SL MED TIFANY SDL')
        os = int(input('Nº OS: '))
        qtde = int(input('Qtde de sacola: '))
        print(f'Qtde de pacotes: {qtde/qtdeMD:.0f}\nPeso: {(qtde/qtdeMD)*pesoMD} Kg\n')
    elif tipo == 8:
        print('SL MED BRANCA SDL')
        os = int(input('Nº OS: '))
        qtde = int(input('Qtde de sacola: '))
        print(f'Qtde de pacotes: {qtde/qtdeMD:.0f}\nPeso: {(qtde/qtdeMD)*pesoMD} Kg\n')

    elif tipo == 9:
        print('SL GRA PRETA SDL')
        os = int(input('Nº OS: '))
        qtde = int(input('Qtde de sacola: '))
        print(f'Qtde de pacotes: {qtde/qtdeGR:.0f}\nPeso: {(qtde/qtdeGR)*pesoGR} Kg\n')
    elif tipo == 10:
        print('SL GRA ROSA SDL')
        os = int(input('Nº OS: '))
        qtde = int(input('Qtde de sacola: '))
        print(f'Qtde de pacotes: {qtde/qtdeGR:.0f}\nPeso: {(qtde/qtdeGR)*pesoGR} Kg\n')
    elif tipo == 11:
        print('SL GRA TIFANY SDL')
        os = int(input('Nº OS: '))
        qtde = int(input('Qtde de sacola: '))
        print(f'Qtde de pacotes: {qtde/qtdeGR:.0f}\nPeso: {(qtde/qtdeGR)*pesoGR} Kg\n')
    elif tipo == 12:
        print('SL GRA BRANCA SDL')
        os = int(input('Nº OS: '))
        qtde = int(input('Qtde de sacola: '))
        print(f'Qtde de pacotes: {qtde/qtdeGR:.0f}\nPeso: {(qtde/qtdeGR)*pesoGR} Kg\n')
    qtdTotal += qtde
print(f'Quatidade total de sacolas: {qtdTotal}')




