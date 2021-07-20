resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    nm = int(input('Digite um número: '))
    soma += nm
    quant += 1
    if quant == 1:
        maior = menor = nm
    else:
        if nm > maior:
            maior = nm
        if nm < menor:
            menor = nm
    resp = str(input('Desja continuar [Y/N]: ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
