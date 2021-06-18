from math import hypot

co = float(input('comprimento do catesto oposto: '))
ca = float(input('Compromento do cateto adjacente: '))
h1 = hypot(co, ca)
print('O comprimento da hipotenusa é: {:.2f}'.format(h1))