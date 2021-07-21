cont = 0
soma = 0
while True:
    nm = int(input(f'Digite o {cont+1}º número: '))
    if nm == 999:
        break
    cont += 1
    soma += nm
print(f'Foram lançados {cont} números, totalizando {soma}')