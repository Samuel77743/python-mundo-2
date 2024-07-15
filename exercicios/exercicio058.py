# Responder até acertar
from random import randint
resp = None

numAleatorio = randint(1, 10)
qtdTentativa = 1

print(f'{"ADVINHE":-^25}')
resp = int(input('Em qual número o computador "pensou"? '))
while resp != numAleatorio:
    qtdTentativa += 1
    if resp == numAleatorio - 1 or resp == numAleatorio + 1:
        resp = int(input('Tá quente, tente novamente -> '))
    else:
        resp = int(input('Tá gelado, tente novamente -> '))

print(f'Acertou! o número era {numAleatorio}.')
print(f'Você tentou: {qtdTentativa} vezes')