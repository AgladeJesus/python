n = s = 0
cont = 1
while True:
    n = int(input('Digite o {}º número: '.format(cont)))
    if n == 999:
        break
    s += n
    cont += 1
print('A soma vale {}, e você lançou {} números'.format(s, cont))
print(f'A soma vale {s}, e você lançou {cont} números')