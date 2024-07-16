# Perguntar ao usuário um número, mostrar contagem e soma

print(f'\033[32m{"SOMADOR":-^25}\033[m')
num = acum = cont = 0
while True:
    num = int(input('Digite o número(999 para sair) -> '))
    if num == 999:
        break
    cont += 1
    acum += num

print(f'Você digitou {cont} números somando {acum}')