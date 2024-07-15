#Fibobacci

qtdTermos = int(input('Quantidade de termos -> '))

t1 = 0
t2 = 1
t3 = None

cont = 3
print(f'{t1} -> {t2} -> ', end='')

while cont <= qtdTermos:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    t1 = t2
    t2 = t3
    cont += 1
