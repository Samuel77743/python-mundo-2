# PEDRA, PAPEL e TESOURA

from random import choice

print(f'{"PEDRA, PAPEL E TESOURA":-^30}')

escolhas = ['Pedra', 'Papel', 'Tesoura']

while True:
    jogador = str(input('SUA RESPOSTA -> ')).capitalize()
    if not(jogador in escolhas):
        print('Resposta Inválida! Tente novamente.')
    else:
        break

cpu = choice(escolhas)

print(f'\n{jogador} X {cpu}')

if jogador == cpu:
    print('{}EMPATE!{}'.format('\033[33m', '\033[m'))

# Vezes que o jogador perde
elif(
(jogador == 'Pedra' and cpu == 'Papel') or
(jogador == 'Papel' and cpu == 'Tesoura') or
(jogador == 'Tesoura' and cpu == 'Pedra')):
    print('{}Jogador Pedeu{}'.format('\033[31m', '\033[m'))

else:
    print('{}Jogador Venceu! Parabéns{}'.format('\033[32m', '\033[m'))


