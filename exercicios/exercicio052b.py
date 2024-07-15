#Divisores exatos dos números

from math import sqrt
resp = int(input('Digite o número: '))

for i in range(2, int(sqrt(resp))):
    print(f'{resp} / {i}...', end=' ')
    print('\033[42mACEITO!' if resp % i == 0 else '\033[41mNEGADO', end='')
    print('\033[m')

print('\nFIM!')