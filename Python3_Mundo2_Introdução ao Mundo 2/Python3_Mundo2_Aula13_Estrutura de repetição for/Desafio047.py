from time import sleep

for c in range(2, 51, 2):
    sleep(0.5)
    print('.', end=' ')
    print(c, end=' ',)

'''for c in range(2, 51):
    if c % 2 ==0:
        print('-', end=' ')
        print(c, end=' ')'''