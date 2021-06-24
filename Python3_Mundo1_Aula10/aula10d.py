n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

media = (n1 + n2 + n3)/3

print('A sua média é: {:.2f}'.format(media))

print('PARABÉNS, VOCÊ VOI APROVADO!' if media >= 7 else 'REPROVADO, ESTUDE MAIS!')