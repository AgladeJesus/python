print('-='*20)
print('CALCULADORA DE PAPEL')
print('-='*20)
print('''
[1] CONVERTER FOLHAS PARA QUILLOS
[2] CONVERTER QUILOS PARA FOLHAS
[3] CONVERTER FOLHAS PARA METRO LINEAR
[4] CONVERTER QUILOS PARA METRO LINEAR
[5] CALCULAR MICRO-ONDULADO FACE SIMPLES
''')
def calc_peso_folha():

    peso = ((larg/1000)*(comp/1000)*(gram/1000))
    return peso

def calc_metroquadrado_folha():

    metroQfl = ((larg / 1000) * (comp / 1000))

    return metroQfl

opção = int(input('O quer você deseja fazer: '))

if opção == 1:
    print('-='*20)
    print('CONVERTER FOLHAS PARA QUILLOS')
    print('-=' * 20)

    larg = int(input('Largura: '))
    comp = int(input('Comprimento: '))
    gram = int(input('Gramatura: '))
    vlrPct = float(input('Valor do pacote: '))
    qtdePct = int(input('Qtde de folhas no pacote: '))

    x = calc_peso_folha()
    #y = calc_metroquadrado_folha()

    qtdefls = int(input('Qtde de folhas: '))
    pesoTfls = x * qtdefls
    print('-=' * 20)
    print('RESUMO DAS INFORMAÇÕES')
    print('-=' * 20)
    print('Peso da folha: '.format(x))
    #print('Area da folha em m²: '.format(y))
    print('Preço unitário da folha: '.format(vlrPct / qtdePct))
    print('Preço do quilos: '.format())
    print('O peso para essa quantidade de folhas é: {:.2f} quilos'.format(pesoTfls))
else:
    print('Em Construção')



