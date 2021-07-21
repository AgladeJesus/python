print('*'*30)
print('CALCULADORA DE PAPEL')
print('*'*30)

def menu():
    print('''\033[31m
        [0] SAIR DO PROGRAMA.
        [1] PESO DA FOLHA E ÁREA EM M².
        [2] TOTAL EM PESO E M² PARA DETERMINADA QTDE DE FOLHAS.
        [3] INFORMAR NOVO FORMATO.\033[m
    ''')

def calc_peso_folha():
    peso = ((larg / 1000) * (comp / 1000) * (gram / 1000))
    return peso

def calc_metroquadrado_folha():
    metroQfl = ((larg / 1000) * (comp / 1000))
    return metroQfl

larg = int(input('Largura: '))
comp = int(input('Comprimento: '))
gram = int(input('Gramatura: '))

while True:
    menu()
    opção = int(input('O quer você deseja fazer: '))
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
        qtdefls = int(input('\033[32mQtde de folhas: \033[m'))
        print(f'\033[32mO peso de uma folha é {calc_peso_folha():.4f} Kg, e o total para {qtdefls} folhas é {qtdefls*calc_peso_folha():.2f} kg\033[m')
        print(f'\033[32mO m² de uma folha é {calc_metroquadrado_folha():.4f} m², e o total para {qtdefls} folhas é {qtdefls*calc_metroquadrado_folha():.2f} m²\033[m')
    elif opção == 3:
        larg = int(input('Largura: '))
        comp = int(input('Comprimento: '))
        gram = int(input('Gramatura: '))
    elif opção == 4:
        vlrPct = float(input('Valor do pacote: '))
        qtdePct = int(input('Qtde de folhas no pacote: '))
        pesoTfls = x * qtdefls
        print('-=' * 20)
        print('RESUMO DAS INFORMAÇÕES')
        print('-=' * 20)
        print('Preço \033[36munitário da folha\033[m: R$ {:.4f}'.format(vlrPct / qtdePct))
        print('Preço do \033[36mQUILO\033[m: R$ {:.4f}'.format(qtdefls * (vlrPct / qtdePct) / pesoTfls))
        print('O \033[36mPESO\033[m para essa \033[36mquantidade de folhas\033[m é: {:.2f} Kg'.format(pesoTfls))
        print('-=' * 20)
        print('Em Construção')
print('FIM DO PROGRAMA')