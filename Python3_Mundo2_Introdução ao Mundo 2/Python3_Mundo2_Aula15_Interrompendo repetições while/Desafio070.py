print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
status = ' '
while status == 'S':
    prod = str(input('Nome do Produto: ')).upper().strip()
    preco = float(input('Preço R$ '))
    status = str(input('Quer Continuar? [S/N]: ')).upper().strip()[0]
    if status == 'N':
        break


