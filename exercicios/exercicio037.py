# Convertendo número para Binário, Octal, e Hexadecimal

import math as m
print(f'{"CONVERSÃO DE BASES NUMÉRICAS":-^30}')

dec = int(input('Digite o número -> '))
quociente = dec
bins = []
while quociente >= 1:
    bins.append(quociente%2)
    quociente / 2

print(f'{dec} em binário é {"".join(bins)}')