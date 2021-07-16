from time import sleep

nm1 = int(input('Digite o primeiro valor: '))
nm2 = int(input('Digite o segundo valor: '))

def menu():
    print('''
[ 1 ] Soma
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
opcao = 0
while opcao != 5:
    menu()
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        somar = nm1 + nm2
        print('O resultado da soma de {} + {} = {}'.format(nm1, nm2, somar))
    elif opcao == 2:
        multiplicar = nm1 * nm2
        print('O produto dos números {} * {} = {}'.format(nm1, nm2, multiplicar))
    elif opcao == 3:
        if nm1 > nm2:
            maior = nm1
        else:
            maior = nm2
        print('Dos números {} e {} digitados, o maior é {}'.format(nm1, nm2, maior))
    elif opcao == 4:
        nm1 = int(input('Digite o primeiro valor: '))
        nm2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('-='*20)

sleep(1)
print('Fim do programa! Volte sempre!')

