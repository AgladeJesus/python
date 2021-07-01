print('-='*40)
print('CALCULADO DE MÉDIA')
print('-='*40)

nm1 = float(input('Digite a sua primeira nota: '))
nm2 = float(input('Digite a sua segunda nota: '))

media = (nm1+nm2)/2

if media < 5.0:
    print('REPROVADO')
elif (media => 5.0) and (media =< 6.9):
    print('RECUPERAÃO')
else:
    print('APROVADO')