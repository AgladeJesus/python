import random

print('*' * 40)
print('SORTEANDO ALGUÉM DA LISTA DE NOMES')
print('*' * 40)

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Qurato aluno: '))

lista = [n1, n2, n3, n4]

escolhido = random.choice(lista)

print('o aluno escolhido foi {}'.format(escolhido))