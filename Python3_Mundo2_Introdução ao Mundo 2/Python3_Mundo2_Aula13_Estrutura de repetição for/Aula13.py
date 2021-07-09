'''for c in range(0, 7, 2):
    print(c)
print('Fim')'''

i = int(input('Número inicial: '))
f = int(input('Número final: '))
p = int(input('Passo na sequencia: '))

for c in range(i, f+1, p):
    print(c)
print('FIM')