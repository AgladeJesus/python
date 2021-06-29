a = int(input('Digite um número: '))
print('O número digitado foi: \033[43m{}\033[m, o seu antecessor é: \033[44m{}\033[m e o seu sucessor é: \33[46m{}\033[m'.format(a,(a-1),(a+1)) )