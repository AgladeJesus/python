from time import sleep

for c in range(0, 51, 2):
    sleep(0.1)
    print('.', end=' ')
    print(c, end=' ',)

print('\n\033[31m')

for c in range(0, 51):
    sleep(0.2)
    if c % 2 ==0:
        print('.', end=' ')
        print(c, end=' ')