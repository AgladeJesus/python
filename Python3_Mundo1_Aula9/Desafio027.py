nome = str(input('Digite seu nome completo: ')).strip().upper()
div = nome.split()
print('Seu primeiro nome é: {}'.format(div[0]))
print('Seu ultimo nome é: {}'.format(div[len(nome)-1]))
