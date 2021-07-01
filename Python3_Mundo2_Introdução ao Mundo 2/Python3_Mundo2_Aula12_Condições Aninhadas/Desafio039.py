import datetime
anoNasc = int(input('Digite o ano do seu Nascimento: '))

ano = datetime.date.today().year
idade = ano - anoNasc
print(idade)