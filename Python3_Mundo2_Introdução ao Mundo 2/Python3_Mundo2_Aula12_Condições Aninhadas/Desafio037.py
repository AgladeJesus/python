print('='*40)
print('{:^40}'.format('CONVERSÃO DE BASES NUMERICAS'))
print('='*40)

nm = int(input('Digite um número para ser convertido: '))
print('''Para qual base deseja converter: 
[1] Binária
[2]Octal
[3]Hexadecimal''')
base = int(input('Digite umas das opções acima: '))

numBin = bin(nm)
numOct = oct(nm)
numHex = hex(nm)

if base == 1:
    print('Número binário é: {}'.format(numBin [2:]))
elif base == 2:
    print('Númenro octal é: {}'.format(numOct [2:]))
else:
    print('Númenro Hexadecimal é: {}'.format(numHex [2:]))