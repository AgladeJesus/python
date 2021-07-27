print('='*50)
print('{:^50}'.format('EMPRÉSTIMO PESSOAL PARA COMPRA DE IMOVÉL'))
print('='*50)

vlrCasa = float(input('Valor da Casa: '))
sal = float(input('Qual a renda mensal: '))
anosPag = int(input('Quantos anos para Pagamento: '))

qtdeParc = anosPag*12
vlrParc = vlrCasa / qtdeParc
percParc30 = sal * (30 / 100)

print(f'Quantidades de Parcelas: R${qtdeParc:.2f}, Valor da Parcela: R${vlrParc:.2f}, Percentual de 30% sobre a renda: R${percParc30}')

if vlrParc < percParc30:
    print('Parabéns! O seu empréstimo foi aprovado.')
else:
    print('Infelizmente o seu empréstimo não foi aprovado!')