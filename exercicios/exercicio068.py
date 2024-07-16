# Par ou Ímpar
from random import randint

print(f'{"PAR OU ÍMPAR":-^20}')

venceu = True
cont = 0
while venceu:
    numJog = int(input('Digite um valor -> '))
    numComp = randint(1, 10)
    numTotal = numComp + numJog

    resp = str(input('Quer PAR ou ÍMPAR [P/I] -> ')).upper()
    while resp not in 'PI':
        resp = str(input('\033[31mResposta inválida! Tente novamente[P/I] -> \033[m')).upper()
    respComp = 'ÍMPAR' if resp == 'P' else 'PAR'

    print(f'\n\033[33m---RESULTADOS---\033[m')
    print(f'Jogador({"PAR" if resp == "P" else "ÍMPAR"}) -> {numJog}')
    print(f'CPU({respComp}) -> {numComp}')
    print(f'TOTAL -> {numTotal}')

    if (
    (numTotal % 2 == 1 and resp == 'P') or
    (numTotal % 2 == 0 and resp == 'I')):
        venceu = False
        break
    cont += 1
    print('\033[32mVocê ganhou.. VAMOS TENTAR NOVAMENTE!\033[m')

print(f'\033[34mGAME OVER - VOCÊ VENCEU \033[4m{cont} vezes!\033[m')
    



