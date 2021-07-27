print('='*40)
print('{:^40}'.format('CONVERSÃO DE BASES NUMERICAS'))
print('='*40)
while True:
    nm = int(input('Digite um número para ser convertido: '))
    if nm == 0:
        break
    print('''Para qual base deseja converter: 
    [1] Binária
    [2]Octal
    [3]Hexadecimal''')
    base = int(input('Digite umas das opções acima: '))

    numBin = bin(nm)
    numOct = oct(nm)
    numHex = hex(nm)

    if base == 1:
        print(f'Número binário é: {numBin [2:]}')
    elif base == 2:
        print(f'Númenro octal é: {numOct [2:]}')
    else:
        print(f'Númenro Hexadecimal é: {numHex [2:]}')
        
print('FIM DO PROGRAMA')





