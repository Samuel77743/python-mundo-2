# Responder até acertar
from random import randint
resp = None

numAleatorio = randint(1, 10)

print(f'{"ADVINHE":-^25}')
while resp != numAleatorio:
    resp = int(input("Tente advinhar o número entre 1 - 10: "))

print(f'O número era o {numAleatorio}')