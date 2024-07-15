#Fogos de artificio
from time import sleep

for i in range(10,-1,-1):
    #Alterando a cor do terminal
    print('\033[31m' if i % 2 == 0 else '\033[32m', end='')

    #Printando a contagem com 1 zero a esquerda
    print(f'{i:02d}')
    sleep(1)

print('\033[m')
print('BOOM!')