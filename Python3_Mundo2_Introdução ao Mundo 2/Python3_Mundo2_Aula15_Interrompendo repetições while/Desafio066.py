cont = 1
nm = soma = 0
while True:
    nm = int(input(f'Digite o {cont}º número: '))
    if nm == 999:
        break
    cont += 1
    soma += nm
print(f'Foram lançados {cont-1} números, totalizando {soma}')