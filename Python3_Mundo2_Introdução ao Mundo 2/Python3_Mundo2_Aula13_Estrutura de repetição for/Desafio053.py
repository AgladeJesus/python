frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
print(palavras)
junto = ''.join(palavras)

inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')
print('A frese digitada é {}, e o contrario foi {}'.format(junto, inverso))
print(letra)