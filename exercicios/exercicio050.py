# Soma dos pares
cont = acum = 0

for i in range(1, 7):
    resp = int(input(f'Digite o {i}º número -> '))
    if resp % 2 == 0:
        acum += resp
        cont += 1

print(f'\nSoma dos {cont} números pares respondidos é -> {acum}')