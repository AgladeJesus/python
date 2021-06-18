celsius = float(input('Digite uma temperatura em ºC: '))
fahrenheit = (celsius * (9/5)) + 32
kelvin = celsius + 273.15
print('A temperatura é: {:.2f} ºF'.format(fahrenheit))
print('A temperatura é: {:.2f} K'.format(kelvin))