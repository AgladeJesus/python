cor = {'limpa':'\33[m',
       'red':'\33[31m',
       'bw':'\033[7;30m',
       'azul':'\033[34m',
       'amarelo':'\033[33m'}

print('========DESAFIO 2 ========')
print('DATA DE NASCIMENTO')

dia = input('Dia: ')
mes = input('Mês: ')
ano = input('ano: ')

print('Você nasceu no dia {}{}{} de {}{}{} de {}{}{} Correto?'.format(cor['red'],dia, cor['limpa'],cor['azul'],mes, cor['limpa'],cor['amarelo'],ano, cor['limpa']))