# Número primo
# Dica: teste 9857
from math import sqrt

resp = int(input('Digite um número -> '))
isPrimo = True

for i in range(2, resp):
    print(f'Testando {resp} / {i}...')
    if resp % i == 0:
        isPrimo = False
        break
    if i > sqrt(resp):
        break

print('\033[42mÉ PRIMO' if isPrimo else '\033[41mNÃO É PRIMO', end='')
print('\033[m')                