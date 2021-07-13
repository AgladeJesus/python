from datetime import date
anoAtual = date.today().year
menor = 0
maior = 0

for c in range(1, 8):
    nm = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if (anoAtual-nm) >= 21:
        maior += 1
    else:
        menor += 1
print('Temos ao todo {} pessoas maiores de idade e {} pessoas menores de idade'.format(maior, menor))