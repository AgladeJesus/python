
def menu():
    print('-='*20)
    print('CALCULADORA DE PAPEL')
    print('-='*20)
    print('''
    [0] PARA SAIR DO PROGRAMA
    [1] CONVERTER FOLHAS PARA QUILLOS
    [2] CONVERTER QUILOS PARA FOLHAS
    [3] CONVERTER FOLHAS PARA METRO LINEAR
    [4] CONVERTER QUILOS PARA METRO LINEAR
    [5] CALCULAR MICRO-ONDULADO FACE SIMPLES
    [6] CALCULAR CHAPA ONDULADA
    [7] CALCULAR QTDE DE TINTA A SER USADA
    ''')

def calc_peso_folha():

    peso = ((larg/1000)*(comp/1000)*(gram/1000))
    return peso

def calc_metroquadrado_folha():
    metroQfl = ((larg / 1000) * (comp / 1000))
    return metroQfl

while True:
    menu()
    opção = int(input('O quer você deseja fazer: '))
    if opção == 0:
        break
    if opção == 1:
        print('-='*20)
        print('CONVERTER FOLHAS PARA QUILLOS')
        print('-=' * 20)

        larg = int(input('Largura: '))
        comp = int(input('Comprimento: '))
        gram = int(input('Gramatura: '))
        vlrPct = float(input('Valor do pacote: '))
        qtdePct = int(input('Qtde de folhas no pacote: '))
        qtdefls = int(input('Qtde de folhas: '))
        
        x = calc_peso_folha()
        y = calc_metroquadrado_folha()
        pesoTfls = x * qtdefls

        print('-=' * 20)
        print('RESUMO DAS INFORMAÇÕES')
        print('-=' * 20)
        print('Peso da folha: {} Kg'.format(x))
        print('Área da folha: {} m²'.format(y))
        print('Preço \033[36munitário da folha\033[m: R$ {:.4f}'.format(vlrPct / qtdePct))
        print('Preço do \033[36mQUILO\033[m: R$ {:.4f}'.format(qtdefls*(vlrPct / qtdePct)/pesoTfls))
        print('O \033[36mPESO\033[m para essa \033[36mquantidade de folhas\033[m é: {:.2f} Kg'.format(pesoTfls))
        print('-=' * 20)
    else:
        print('Em Construção')
print('FIM DO PROGRAMA')
