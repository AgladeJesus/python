print('-='*20)
print('CALCULADORA DE PAPEL')
print('-='*20)

tipo = str(input('Digite o tipo de Substrato: ')).upper()
qtdefls = int(input('Quantidade de folhas: '))
larg = int(input('Largura: '))
comp = int(input('Comprimento: '))
gram = int(input('Gramatura: '))

print('Descrição: Papel {}, nas dimenssões {}mm x {}mm - {}g para quantidade: {} folhas.'.format(tipo, larg, comp, gram, qtdefls))



