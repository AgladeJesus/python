print('='*30)
print('{:^30}'.format('BANCO AGLA DE JESUS'))
print('='*30)

valor = int(input('Valor do saque: R$ '))
total = valor
céd = 100
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd+= 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 100:
            céd = 50
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 2
        elif céd == 2:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre am Banco Agla de Jesus! Tenha um bom dia!')
