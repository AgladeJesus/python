print('-='*20)
print('TABUADA')
print('-='*20)
nm1 = 0
while True:
    nm1 = int(input('Você deseja a TABUADA de qual número: '))
    if nm1 < 0:
        break
    cont = 1
    while cont <= 10:
        print(f'{nm1} x {cont} = {nm1*cont}')
        cont += 1