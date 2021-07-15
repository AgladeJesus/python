n = 1
somapar = 0
somaimpar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            somapar += 1
        if n % 2 == 1:
            somaimpar += 1
print('A soma de todos os números pares é {}, e a todos impares são {}.'.format(somapar, somaimpar))
print('Acabou')