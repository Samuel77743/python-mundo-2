# Ler 2 valores e perguntar se deseja: somar, multiplicar, saber maior
# testar novos números ou sair do programa
nums = []
resp = None

for i in range(1, 3):
    nums.append(int(input(f'{i}º número -> ')))

while resp not in [1, 2, 3, 4, 5]:
    print(f'{"MENU":-^25}', end='')
    print("""
    [1] SOMAR
    [2] MULTIPLICAR
    [3] SABER MAIOR
    [4] TESTAR NOVOS NÚMEROS
    [5] SAIR
    """
    )
    resp = int(input('SUA RESPOSTA -> '))

    if resp == 1:
        print(f'A SOMA DE {nums[0]} + {nums[1]} = {nums[0] + nums[1]}')

    elif resp == 2:
        print(f'A MULTIPLICAÇÃO DE {nums[0]} * {nums[1]} = {nums[0] * nums[1]}')

    elif resp == 3:
        if nums[0] == nums[1]:
            print('São iguais')
            break
        print(f'{nums[0]} é maior' if nums[0] > nums[1] else f'{nums[1]} é maior')

    elif resp == 4:
        print('Digite os novos números:')
        nums[0] = int(input('1º número -> '))
        nums[1] = int(input('2º número -> '))
        resp = None

    elif resp == 5:
        break

print(f'\n{"FIM DO PROGRAMA":-^20}')