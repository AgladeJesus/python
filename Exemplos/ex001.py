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
    larg = int(input('Largura: '))
    comp = int(input('Comprimento: '))
    gram = int(input('Gramatura: '))

    peso = ((larg/1000)*(comp/1000)*(gram/1000))
    return peso

opção = int(input('O quer você deseja fazer: '))

if opção == 1:
        x = calc_peso_folha()
        qtdefls = int(input('Qtde de folhas: '))
        pesoTfls = x * qtdefls
        print('O peso para essa quantidade de folhas é: {:.2f} quilos'.format(pesoTfls))
else:
    print('Em Construção')



