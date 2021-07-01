from datetime import date

anoNasc = int(input('Digite o ano do seu Nascimento: '))

ano = date.today().year
idade = ano - anoNasc

if idade < 18:
    print('Quando completar 18 anos, procure os serviços de alistamento militar')
elif idade == 18:
    print('Você pode se alistar')
else:
    print('Apresente-se aos serviços militar para dar baixo, pois você passou o tempo de se alistar')

