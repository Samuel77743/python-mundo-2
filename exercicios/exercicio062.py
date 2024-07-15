# PA elaborada

print(f'{"PROGRESSÃO ARITMÉTICA - MK III":=^30}')
a1 = int(input('Termo inicial -> '))
razao = int(input('Razão(incremento) -> '))
cont = 1
termo = a1
totalTermos = 10

print(f'{"10 TERMOS":-^30}')
while cont <= 10:
    print(f'{termo}', end=' -> ' if cont != 10 else ' FIM!')
    termo += razao
    cont += 1

resp = None
while resp != 0:
    resp = int(input('\nGostaria de imprimir mais quantos? '))
    totalTermos += resp

    print(f'{f"IMPRIMINDO MAIS {resp} ELEMENTOS":=^30}')
    while cont <= totalTermos:
        print(f'{termo}', end=' -> ' if cont != totalTermos else ' FIM!')
        termo += razao
        cont += 1

print(f'\n{totalTermos} termos impressos')
print('---FIM DO PROGRAMA---')