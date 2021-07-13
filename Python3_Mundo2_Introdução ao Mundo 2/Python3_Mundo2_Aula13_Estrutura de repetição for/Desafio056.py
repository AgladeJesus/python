somaIdade = 0
cont1 = 0 
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    somaIdade += idade
    cont1 += 1
media = somaIdade / cont1

print('A média de idade do grupo é de {} anos'.format(media))