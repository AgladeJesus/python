print('*'*30)
print('CALCULADORA DE PAPEL')
print('*'*30)

largFl = int(input('Largura: '))
compFl = int(input('Comprimento: '))
gram = int(input('Gramatura: '))
qtdaFls = 0

def menu():
    print('''\033[31m
        [0] SAIR DO PROGRAMA.
        [1] PESO DA FOLHA E ÁREA EM M².
        [2] TOTAL EM PESO E M² PARA DETERMINADA QTDE DE FOLHAS.
        [3] INFORMAR NOVO FORMATO.\033[m
    ''')

def calc_peso_folha():
    peso = ((largFl / 1000) * (compFl / 1000) * (gram / 1000))
    return peso
def calc_metroquadrado_folha():
    metroQfl = ((largFl / 1000) * (compFl / 1000))
    return metroQfl
def calc_peso_total():
    pesoTotal = qtdeTotal() * calc_peso_folha()
    return pesoTotal
def qtdeTotal():
    qtdefls = int(input('Quantidade Total: '))
    return qtdefls

menu()

while True:
    opção = int(input('Informe sua opção: '))
    if opção == 0:
        break
    if opção == 1:
        print('-=' * 20)
        print('PESO DA FOLHA')
        print('-=' * 20)
        print('\033[36mPeso da folha: {:.4f} Kg\033[m'.format(calc_peso_folha()))
        print('\033[36mÁrea da folha: {:.4f} m²\033[m'.format(calc_metroquadrado_folha()))
    elif opção == 2:
        print('-=' * 20)
        print('TOTAL EM PESO E M² PARA DETERMINADA QTDE DE FOLHAS')
        print('-=' * 20)
        tfls = qtdeTotal()
        #qtdefls = int(input('\033[32mQtde de folhas: \033[m'))
        print(f'\033[32mO peso de uma folha é {calc_peso_folha():.4f} Kg, e o total para {tfls} folhas é {tfls*calc_peso_folha():.2f} kg\033[m')
        print(f'\033[32mO m² de uma folha é {calc_metroquadrado_folha():.4f} m², e o total para {tfls} folhas é {tfls*calc_metroquadrado_folha():.2f} m²\033[m')
    elif opção == 3:
        larg = int(input('Largura: '))
        comp = int(input('Comprimento: '))
        gram = int(input('Gramatura: '))
    elif opção == 4:
        print(f'Quantidade de folhas: {qtdeTotal()}')
        print(f'Peso Total: {calc_peso_total():.2f} kg,')
print('FIM DO PROGRAMA')