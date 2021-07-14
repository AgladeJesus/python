i = 0
c = 'S'
while i < 10:
  i += 1
  c = str(input('Deseja continuar: [Y/N]: '))
  if c == 'N':
    break
print(i)