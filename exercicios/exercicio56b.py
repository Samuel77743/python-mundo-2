# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: 
# a média de idade do grupo,
# qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.

acumIdade = 0
maiorIdadeM = 0
nomeVelho = ''
acumIdadeF = 0

for i in range(1, 5):
    print(f'{i}º Pessoa:')
    nome = str(input('NOME -> ')).title()
    idade = int(input('IDADE -> '))
    sexo = str(input('SEXO -> ')).upper()

    acumIdade += idade

    if sexo == 'M':
        if idade > maiorIdadeM:
            maiorIdadeM = idade
            nomeVelho = nome
    else:
        if idade < 20:
            acumIdadeF += 1

media = acumIdade / 4
print(f'MÉDIA DA IDADE: {media}')
print(f'HOMEM MAIS VELHO: {nomeVelho}')
print(f'QTD. MULHERES COM MENOS DE 20: {acumIdadeF}')