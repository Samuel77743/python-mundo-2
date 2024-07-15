from math import sqrt

print(f'{"NÚMERO PRIMO?":-^25}')
resp = int(input('Digite o número -> '))

isPrimo = True
for i in range(2, int(sqrt(resp))):
    print(f'ANALISANDO {resp} / {i}...')
    if resp % i == 0:
        isPrimo = False
        break

print(f'É PRIMO' if isPrimo else 'NÃO É PRIMO')
