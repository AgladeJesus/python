print('-='*20)
print('CONVERSÃO DE BASES NUMERICAS')
print('-='*20)

nm = int(input('Digite um número para ser convertido: '))
base = int(input('Para qual base deseja converter: [1]Binária | [2]Octal | [3]Hexadecimal'))

numBin = bin(nm)
numOct = oct(nm)
numHex = hex(nm)

if base == 1:
    print('Número binário é: {}'.format(numBin))
elif base == 2:
    print('Númenro octal é: {}'.format(numOct))
else:
    print('Númenro Hexadecimal é: {}'.format(numHex))