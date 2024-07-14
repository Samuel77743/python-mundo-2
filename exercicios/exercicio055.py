# Maior em enor peso lidos
print(f'{"MAIOR E MENOR PESO":=^30}')

maiorPeso = 0
menorPeso = 0
for i in range(1, 6):
    resp = float(input(f'Informe o {i}º peso -> '))
    if i == 1:
        maiorPeso = resp
        menorPeso = resp
    else:
        if resp > maiorPeso:
            maiorPeso = resp
            continue #Otimização
        if resp < menorPeso:
            menorPeso = resp

print(f'\n{"CONCLUSÃO":-^30}')
print(f'Maior peso: {maiorPeso}kg')
print(f'Menor peso: {menorPeso}kg')