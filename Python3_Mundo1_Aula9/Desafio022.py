nome = str(input('Digite o seu nome completo: ')).strip()

print('Analisando seu nome...')
print('Seu nome em letras maiúcula é: {}'.format(nome.upper()))
print('Seu nome em letras minúscula é: {}'.format(nome.lower()))
print('Seu nome tem ao todos tem {} letras'.format(len(nome) - nome.count(' ')))
div = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(div[0], len(div[0])))
