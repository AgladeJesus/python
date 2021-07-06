print('-='*20)
print('CONDIÇÕES DE PAGAMENTO')
print('-='*20)

print('-='*20)
print('CONDIÇÕES DE PAGTO')
print('-='*20)
print('[1] À vista no dinheiro ou cheque, 10% de desconto.')
print('[2] À vista no Cartão, 5% de desconto.')
print('[3] Parcelado em 2 vezes sem juros.')
print('[4] Parcelado em 3 vezes com 20% de juros.\n\n')

vlr = float(input('Valor total da sua compra: '))
cp = int(input('Qual condição de Pagto você prefere? '))

if cp == 1:
    print('Valor final a Pagar: R${:.2f}'.format(abs(vlr * ((10/100)-1))))
elif cp == 2:
    print('Valor final a Pagar: R${:.2f}'.format(abs(vlr * ((5/100)-1))))
elif cp == 3:
    print('Valor final a Pagar: 2 parcelas de R${:.2f}'.format(vlr / 2))
elif cp == 4:
    print('Valor final a Pagar: 3 parcelas de R${:.2f}'.format((vlr * ((20/100)+1))/3))



