print('{:-^40}'.format('LOJA SUPER BARATÃO'))

precoT = maior1000 = menorpreco = cont = 0
barato = ' '
while True:
    prod = str(input('Nome do Produto: ')).upper().strip()
    preco = float(input('Preço R$ '))
    cont += 1
    precoT += preco
    if preco > 1000:
        maior1000 += 1
    '''if cont == 1:
        menorpreco = preco
        barato = prod
    else:
        if preco < menorpreco:
            menorpreco = preco
            barato = prod'''

    if cont == 1 or preco < menorpreco:
        menorpreco = preco
        barato = prod

    status = ' '
    while status not in 'SN':
        status = str(input('Quer Continuar? [S/N]: ')).upper().strip()[0]
    if status == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R$ {precoT:.2f}')
print(f'Temos {maior1000} produto custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R${menorpreco:.2f}')




