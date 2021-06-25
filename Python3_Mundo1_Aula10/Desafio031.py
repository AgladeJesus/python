nm = int(input('Qual a distânica em quilômetro da sua viagem: '))
ate200 = nm * 0.50
acima200 = nm * 0.45
if nm <= 200:
    print('O valor da sua viagem será R${:.2f}'.format(ate200))
else:
    print('O valor da sua viagem será R${:.2f}'.format(acima200))