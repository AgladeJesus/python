print('-='*20)
print('TIPOS DE TRIÂNGULOS')
print('-='*20)

a = float(input('Primeito lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))

if (a + b < c) or (a + c < b) or (b + c < a):
    print('Esses tamanhos não formam um triângulo.')
elif ( a == b) and (a == c):
    print('Triángulo Equilátero')
elif (a == b) or (a == c) or (b ==c):
    print('Triángulo Isósceles')
else:
    print('Escaleno')

