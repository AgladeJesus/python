from datetime import date

anoNasc = int(input('Digite o ano do seu Nascimento: '))

ano = date.today().year
idade = ano - anoNasc


print('Idade atual: {} anos'.format(idade))
if idade < 18:
    print('Falta {} anos, para o alistamento militar'.format(18 - idade))
elif idade == 18:
    print('Apresente-se imediatamente aos postos de alistamento militar.')
else:
    print('Apresente-se aos postos de alistamento militar, você está com {} anos de atraso para cumprir esse requisito.'.format(idade - 18))

