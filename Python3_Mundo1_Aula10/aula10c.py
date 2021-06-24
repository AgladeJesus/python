n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

media = (n1 + n2 + n3)/3

print('A sua média é: {:.2f}'.format(media))

if media >= 7:
    print('Parabéns! Você foi APROVADO! a sua média foi {:.2f}'.format(media))
else:
    print('Caro aluno, a sua média {:.2f}, foi abaixo da meta, você está REPROVADO!'.format(media))