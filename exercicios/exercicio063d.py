seq = [0, 1]
cont = 1
qtd = int(input('Qual a qtd de elementos -> '))
while cont <= qtd - 2:
    seq.append(seq[cont-1] + seq[cont])
    cont += 1

for i in seq:
    print(f'{i} -> ', end='')