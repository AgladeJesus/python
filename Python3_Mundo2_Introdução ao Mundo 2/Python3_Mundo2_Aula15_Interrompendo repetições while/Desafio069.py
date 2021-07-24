print('-='*20)
print('CADASTRO DE PESSOAS')
print('-='*20)
totPes18 = 0
totH = 0
totM20 = 0
while True:
    idade = 0
    while idade <= 0:
        idade = int(input('Idade: '))
    sx = ' '
    while sx not in 'MF':
        sx = str(input('Sexo: [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        totPes18 += 1
    if sx == 'M':
        totH += 1
    if idade < 20 and sx == 'F':
        totM20 += 1
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Deseja continuar: [S/N]: ')).strip().upper()[0]
    if perg == 'N':
        break
print(f'Foram cadastradas {totPes18} pessoas acima de 18 anos')
print(f'A quantidade de homens cadastrados é: {totH}')
print(f'A quantidade de mulheres menor de 20 anos é: {totM20}')
