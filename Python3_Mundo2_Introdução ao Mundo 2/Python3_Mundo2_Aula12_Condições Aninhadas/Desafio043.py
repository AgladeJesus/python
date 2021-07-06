print('-='*20)
print('CALCULADORA DE IMC')
print('-='*20)

peso = float(input('Qual o seu peso: '))
altura = float(input('Qual sua altura: '))

imc = (peso / (altura * altura))

if imc < 18.5:
    print('MAGREZA COM IMC {:.2f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('NORMAL COM IMC {:.2f}'.format(imc))
elif imc >= 25 and imc < 30:
    print('SOBREPESO COM IMC {:.2f}'.format(imc))
elif imc >= 30 and imc < 40:
    print('OBESIDADE COM IMC {:.2f}'.format(imc))
else:
    print('OBESIDADE MÓRBIDA COM IMC {:.2f}'.format(imc))