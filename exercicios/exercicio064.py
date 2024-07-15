# Acumulador
print(f'{"ACUMULADOR":-^50}')
acum = 0
cont = 0
while True:
    resp = int(input('Digite um número [999 para parar] -> '))
    if resp != 999:
        acum += resp
        cont += 1
    else:
        break

print(f'\n{"CONCLUSÃO":-^50}')
print(f'Você digitou {cont} números que somam: {acum}')
