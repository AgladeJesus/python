dias = int(input('Quantos dias o ficou alugado: '))
km = float(input('Quantos quilometros o carro percorreu? '))
aluguel = float(dias*60 + km*0.15)

print('O aluguel do carro em {} dias e {}km custa: R${:.2f}'.format(dias, km, aluguel))