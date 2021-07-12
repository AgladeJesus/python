cont = 0
soma = 0
for c in range(1, 7):
    nm = int(input('Digite o {}º número: '.format(c)))
    if nm % 2 == 0:
        soma = soma + nm
        cont = cont + 1
print('Você informou {} números pares, e a soma deles é: {}'.format(cont, soma))
