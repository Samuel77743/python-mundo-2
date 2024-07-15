
from math import factorial

resp = int(input('Número -> '))
cont = resp 

print(f'Calculando {resp}! =', end=' ')
while cont >= 1:
    if cont != 1:
        print(f'{cont} x', end=' ')
    else:
        print(f'{cont} =', end=' ')
    cont -= 1
print(factorial(resp))