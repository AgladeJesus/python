print('-='*20)
print('CADASTRO DE PESSOAS')
print('-='*20)

while True:
    idade = 0
    while idade <= 0:
        idade = int(input('Idade: '))
    sx = ' '
    while sx not in 'MF':
        sx = str(input('Sexo: [M/F]: ')).upper().strip()[0]
    perg = str(input('Deseja continuar: [S/N]: ')).strip().upper()
    if perg == 'S':
        idade = 0
        while idade <= 0:
            idade = int(input('Idade: '))
        sx = ' '
        while sx not in 'MF':
            sx = str(input('Sexo: [M/F]: ')).upper().strip()[0]
    else:
        break
