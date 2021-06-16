a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

soma = a + b
mult = a * b
sub = a - b
div = a / b
restInt = a // b
rest = a % b

print('A Soma de {} e {}, é igual: {} '.format(a, b, soma))
print('A Multiplicação de {} e {}, é igual: {} '.format(a, b, mult))
print('A Subtração de {} e {}, é igual: {} '.format(a, b, sub))
print('A Divisão de {} e {}, é igual: {} '.format(a, b, div))
print('A parte inteira da divisão de {} e {}, é igual: {} '.format(a, b, restInt))
print('O resto da divisão de {} e {}, é igual: {} '.format(a, b, rest))