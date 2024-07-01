#Pedra Papel e Tesoura
from random import choice
from time import sleep

escolhas = ['Pedra', 'Papel', 'Tesoura']
print(f'{"PEDRA, PAPEL & TESOURA":-^30}')

escolhaCPU = choice(escolhas)
while True:
    escolhaJogador = str(input('Qual a sua escolha? ')).title()
    if not(escolhaJogador in escolhas):
        print('Digite uma opção válida')
        continue
    break

print(f'{"JO":<7}')
sleep(0.5)
print(f'{"KEN":^7}')
sleep(0.5)
print(f'{"PO":<7}')

print(f'{escolhaJogador} VS. {escolhaCPU}')
if escolhaJogador == escolhaCPU:
    print('\033[33mEMPATE\033[m')
elif(
escolhaJogador == 'Pedra' and escolhaCPU == 'Tesoura' or
escolhaJogador == 'Tesoura' and escolhaCPU == 'Papel' or
escolhaJogador == 'Papel' and escolhaCPU == 'Pedra'):
    print('\033[32mJOGADOR VENCEU!\033[m')

else:
    print('\033[31mJOGADOR PERDEU!\033[m')    