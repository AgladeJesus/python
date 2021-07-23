print('-='*20)
print('CADASTRO DE PESSOAS')
print('-='*20)

while True:
  #  idade = int(input('Qual idade: ')
    sx = ' '
    while sx not in 'mf':
        sx = str(input('Digite o sexo [M/F]: '))
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ìmpar: [P/I]: ')).strip().upper()[0]
