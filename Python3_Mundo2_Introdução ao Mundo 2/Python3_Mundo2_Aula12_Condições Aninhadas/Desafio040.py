print('-='*40)
print('CALCULADO DE MÉDIA')
print('-='*40)

nm1 = float(input('Digite a sua primeira nota: '))
nm2 = float(input('Digite a sua segunda nota: '))
nm3 = float(input('Digite a sua terceira nota: '))
nm4 = float(input('Digite a sua quarto nota: '))

media = (nm1+nm2+nm3+nm4)/4
print(f'As notas do aluno são: {nm1}, {nm2},{nm3} e {nm4} resultando na seguinte média: {media:.2f}')
if media < 5.0:
    print('REPROVADO')
elif (media >= 5.0) and (media <= 6.9):
    print('RECUPERAÇÃO')
else:
    print('APROVADO')