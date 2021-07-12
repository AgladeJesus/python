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

tipo = str(input('Digite o tipo de Substrato: ')).upper()
qtdefls = int(input('Quantidade de folhas: '))
larg = int(input('Largura: '))
comp = int(input('Comprimento: '))
gram = int(input('Gramatura: '))

print('Descrição: Papel {}, nas dimenssões {}mm x {}mm - {}g para quantidade: {} folhas.'.format(tipo, larg, comp, gram, qtdefls))



