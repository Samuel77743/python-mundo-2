# Pode-se formar um triângulo
# Se sim, qual a categoria?

print(f'{"TRIÂNGULOS":-^20}')
lado = []
i = 1
while i <= 3:
    lado.append(int(input(f'Tamanho do {i}º lado -> ')))
    i += 1

print(f'\n{"CONCLUSÃO":-^20}')
i = 0
while i < 3:
    print(f'Medida do {i+1}º lado --> {lado[i]}')
    i += 1

if(
lado[0] > lado[1] + lado[2] or
lado[1] > lado[0] + lado[2] or
lado[2] > lado[0] + lado[1]):
    print('Não é possível formar um triângulo com essas medidas!')

else:
    
    print('\nÉ possível formar um Triângulo ', end='\033[42m')
    if(lado.count(lado[0]) == 3):
        print('Equilatero')
        
    elif (
    lado.count(lado[0]) == 2 or
    lado.count(lado[1]) == 2):
        print('Isósceles')
    
    else:
        print('Escaleno')

print('\033[m', end='')

# Alternativa para testar se é Equilatero:
# if(lado[0] == lado[1] and lado[1] == lado[2]):
