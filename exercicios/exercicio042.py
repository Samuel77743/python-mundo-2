# É possível formar um triângulo, de qual tipo?

print(f'{"ANALISANDO TRIÂNGULOS":=^25}')
lados = []
cont = 0

while cont < 3:
    lados.append(int(input(f'Qual o tamanho do {cont+1}º lado? ')))
    cont += 1

print(f'\nMedidas: {lados}', end='\n\n')
if(
lados[0] <= lados[1] + lados[2] and
lados[1] <= lados[0] + lados[2] and
lados[2] <= lados[0] + lados[1]): 

    if lados.count(lados[0]) == 3:
        print('Triâgulo Equilátero')
    elif lados.count(lados[0]) == 2 or lados.count(lados[1]) == 2:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')

else:
    print('Não é possível formar um triângulo com essas medidas!')