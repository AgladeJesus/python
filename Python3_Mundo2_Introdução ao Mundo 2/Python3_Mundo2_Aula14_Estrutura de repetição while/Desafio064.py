soma = 0
cont = 0
nm = 0
nm = int(input('Digite 999 para parar: '))
while nm != 999:
    soma += nm
    cont += 1
    nm = int(input('Digite 999 para parar: '))
print('A soma dos {} números infomardos são: {}.'.format(cont, soma))