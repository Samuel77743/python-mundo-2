# Números pares entre 1 - 50

# Maneira otimizada
for i in range(2, 51, 2):
    print(f'{i:02d}')


# Maneira com custo computacional maior e desnecessário:
for i in range(1, 51, 1):
    print(f'{i:02d}' if i % 2 == 0 else 'X')