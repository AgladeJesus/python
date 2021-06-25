km = int(input('Qual velocidade média do carro?'))

if km > 80:
    print('ATENÇÃO! Você ultrapassou a velocidade permitida desta avenida. \nVelocidade permitida: {}km\h \nTotal ultrapassado: {}km/h \nMulta à pagar: R${}'.format(80, (km-80), ((km-80)*7)))
