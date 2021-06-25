from random import randrange

rdpc = randrange(0, 5)
nm = int(input('Adivinhe qual número que o PC pensou: '))

if nm == rdpc:
    print('PARABÉNS, VOCÊ ACETOU!')
else:
    print('TENTE NOVAMENTE, O NÚMERO NÃO É ESSE.')

print(rdpc)

