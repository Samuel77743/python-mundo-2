qtd = int(input('Quantos termos a serem impressos: '))

t1 = 0
t2 = 1
print(f'{t1} -> {t2} -> ', end='')

t3 = 0
for i in range(3, qtd + 1):
    t3 = t1 + t2
    print(f'{t3}', end=' -> ' if i < qtd else ' FIM!')
    t1 = t2
    t2 = t3