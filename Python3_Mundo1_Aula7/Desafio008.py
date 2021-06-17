m = int(input('Digite uma medida em metros: '))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('=' * 40)
print('SEGUE ABAIXO RESULTADO DA CONVERSÃO')
print('=' * 40)
print('KM: {} \nHM: {} \nDAM: {} \nM: {} \nDM: {} \nCM: {} \nMM: {} \n'.format(km, hm, dam, m, dm, cm, mm))

