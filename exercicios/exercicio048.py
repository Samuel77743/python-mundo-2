# Números entre 1 - 500 que são ímpares e divisíveis por 3
acum = 0
cont = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        print(i)
        acum += i
        cont += 1
    else:
        print('\033[41mX\033[m')

print(f'\nQuantidade de números considerados: {cont}')
print(f'\033[43;31mSoma total dos números: {acum}\033[m')