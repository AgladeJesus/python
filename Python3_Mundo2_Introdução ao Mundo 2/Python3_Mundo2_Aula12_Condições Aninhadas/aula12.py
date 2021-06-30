nome = str(input('Qual é su nome: '))
if nome == 'Alexandre':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
elif nome == 'Arthur' or 'Gleiciane' or 'Lohanny':
    print('Esse nome compõem a família Agla de Jesus')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia,'.format(nome))