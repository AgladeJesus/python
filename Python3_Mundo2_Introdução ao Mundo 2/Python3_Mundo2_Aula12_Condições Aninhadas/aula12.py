while True:
    nome = ' '
    nome = str(input('Qual é su nome: ')).capitalize().strip()
    if nome == 'Alexandre':
        print('Que nome bonito!')
    elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
        print('Seu nome é bem popular no Brasil.')
    elif nome in 'Ana Cláudia Jéssica Juliana':
        print('Belo nome feminino')
    elif nome == 'Arthur' or nome == 'Gleiciane' or nome == 'Lohanny':
        print('Esse nome compõem a família Agla de Jesus')
    elif nome != 'Exit':
            print('Seu nome é bem normal.')
    else:
        break
print('Tenha um bom dia,'.format(nome))