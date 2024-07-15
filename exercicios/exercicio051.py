#Primeiros 10 termos de uma PA
#Fórmula de descobrir o enésimo termo -> an = a1 + (qtd - 1) * razao

# Primeiro método:
valorInicial = int(input('Informe o valor inicial -> '))
razao = int(input('Informe a razão -> '))
enesimo = valorInicial + (10 - 1) * razao

for i in range(valorInicial, enesimo + razao, razao):
    print(f'{i}', end=' -> ')
print('ACABOU!')

# Meu método:
acum = valorInicial
for i in range(1,11):
    print(f'{acum}', end=' -> ')
    acum += razao

print('ACABOU!')