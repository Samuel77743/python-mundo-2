#P.A. - Primeiros 10 termos
#Fórmula -> an = a1 + (qtd - 1) * razao

print(f'{"PROGRESSÃO ARITMÉTICA":-^30}')
a1 = int(input('Informe o valor inicial -> '))
razao = int(input('Informe a razão -> '))
an = a1 + (10 - 1) * razao
cont = a1

while cont <= an:
    print(f'{cont}', end=f' -> ' if cont != an else '\nFIM!')
    cont += razao