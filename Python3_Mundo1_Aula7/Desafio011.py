larg = float(input('Digite a largura da Parede a ser pintada: '))
alt = float(input('Digite a altura da parede a ser pintada: '))
area = larg * alt
lt = 2
tinta = area / lt

print('=' * 50)
print('CALCULO DE TINTA À SER USADA PARA PINTURA DE PAREDE')
print('=' * 50)
print('Largura: {}m'.format(larg))
print('Altura: {}m'.format(alt))
print('Aréa total: {}m²'.format(area))
print('Será necessario de: {} litros de tinta'.format(tinta))
print('=' * 20)
