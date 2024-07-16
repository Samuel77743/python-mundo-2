# Sacando cédulas
# Há cédulas em R$ de: 50, 20, 10 e 1 
print('~'*25)
print(f'{"BANCO SCOOBY":-^25}')
print('~'*25)

valorSaque = float(input('Quanto deseja sacar: R$ '))

somaValor = cont50 = cont20 = cont10 = cont5 = cont1 = 0
cedulaAtual = 50
while True:
    if (somaValor + 50) <= valorSaque:
        somaValor += 50
        cont50 += 1
    elif (somaValor + 20) <= valorSaque:
        somaValor += 20
        cont20 += 1
    elif (somaValor + 10) <= valorSaque:
        somaValor += 10
        cont10 += 1
    elif (somaValor + 5) <= valorSaque:
        somaValor += 5
        cont5 += 1
    elif (somaValor + 1) <= valorSaque:
        somaValor += 1
        cont1 += 1
    else:
        break

print(f'\n{"CONCLUSÃO":-^25}')
print(f"""
CÉDULAS DE R$ 50,00....... {cont50}
CÉDULAS DE R$ 20,00....... {cont20}
CÉDULAS DE R$ 10,00....... {cont10}
CÉDULAS DE R$ 5,00........ {cont5}
CÉDULAS DE R$ 1,00........ {cont1}
""")