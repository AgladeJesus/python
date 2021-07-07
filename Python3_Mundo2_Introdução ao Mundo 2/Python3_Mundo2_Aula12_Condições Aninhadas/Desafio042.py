print('-='*20)
print('TIPOS DE TRIÂNGULOS')
print('-='*20)

a = float(input('Primeito lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))

if (a < b + c) and (b < a + c) and (c < a + b):
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if a == b == c:
        print('Equilátero')
    elif a != b != c != a:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os segmentos acima não PODEM FORMAR um triânglo.')

