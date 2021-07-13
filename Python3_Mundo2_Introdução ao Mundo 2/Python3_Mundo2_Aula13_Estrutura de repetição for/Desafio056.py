somaIdade = 0
media = 0
cont1 = 0 
maiorIdadeHomem = 0
nomeVelho = 0
totmulher = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    somaIdade += idade
    cont1 += 1
    if c == 1 and sexo in 'Mn':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mn' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
media = somaIdade / cont1

print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdadeHomem, nomeVelho))
print('Temos {} mulheres a baixo de 20 amos.'.format(totmulher))