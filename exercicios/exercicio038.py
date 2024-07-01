#Os números são iguais, maiores ou menores?

contador = 1
numeros = []

print(f'{"Comparando Números":=^30}')
while contador <= 2:
    num = int(input(f'{contador}º número -> '))
    numeros.append(num)

    contador += 1

if numeros[0] == numeros[1]:
    print(f'Os números {numeros[0]} e {numeros[1]} são iguais!')
elif numeros[0] > numeros[1]:
    print(f'Os número {numeros[0]} é maior que {numeros[1]}')
else:
    print(f'Os número {numeros[0]} é menor que {numeros[1]}')