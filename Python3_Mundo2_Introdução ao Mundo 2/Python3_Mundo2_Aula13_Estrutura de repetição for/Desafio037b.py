print('='*40)
print('{:^40}'.format('CONVERSÃO DE BASES NUMERICAS'))
print('='*40)
while True:
    nm = int(input('Digite um número para ser convertido: '))
    '''    if nm == 0:
        break'''
    print(f'Número binário é: {bin(nm)[2:]}')
    print(f'Númenro octal é: {oct(nm)[2:]}')
    print(f'Númenro Hexadecimal é: {hex(nm)[2:]}')
print('FIM DO PROGRAMA')