cart = float(input('Qual valor você tem na carteira? '))
usd_hj = 3.27
conv = cart / usd_hj

print('Valor que tenho na Carteira é: R$ {} \nValor de dólar de hoje é: R$ {:.2f} \nCom o que tenho consigo comprar USD {:.2f}'. format(cart, usd_hj, conv))