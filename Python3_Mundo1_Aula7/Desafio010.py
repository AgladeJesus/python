cart = float(input('Qual valor você tem na carteira? '))
usd_hj = float(input('Digite o valor do dálar de hoje: '))
conv = cart // usd_hj
rest = cart % usd_hj

print('Valor que tenho na Carteira é: R$ {} \nValor de dólar de hoje é: R$ {} \nCom o que tenho consigo comprar USD {} \n E Sobrará R$ {:.2f} de Troco'. format(cart, usd_hj, conv, rest))