nome = str(input('Digite o seu nome: ')).strip().upper()
print('A letra A aparece {} vezes na frese.'.format(nome.upper().count('A')))
print('A primeira letra está na posição {}'.format(nome.find('A')+1))
print('A ultima letra está na posição {}'.format(nome.rfind('A')+1))