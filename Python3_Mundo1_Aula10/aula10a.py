tempo = int(input('Quanto tempo tem o seu carro? '))

if tempo <= 3:
    print('Seu carros está novo, com apenas {} anos de idade'.format(tempo))
else:
    print('Seu carro está velho, com {} anos de idade'.format(tempo))
print('FIM')