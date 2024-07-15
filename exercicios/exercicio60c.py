# Fatorial usando FOR

resp = int(input('Digite o número -> '))

resultado = 1
for i in range(resp, 0, -1):
    resultado *= i
    print(f'{i} {"x " if i > 1 else "= "}', end='')
print(resultado)