# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: 
# a média de idade do grupo,
# qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.

print(f'{"ANALISADOR":-^30}')

idadeAnterior = 0
acumIdade = 0
nomeVelho = ''
mulVinte = 0
qtdHomens = 0

for i in range(1, 5):
    print(f'{f"{i}º Pessoa":-^30}')
    nome = input('NOME -> ') 
    idade = int(input('IDADE -> '))
    acumIdade += idade 

    sexo = str(input('SEXO[M/F] -> ')).upper() 

    if sexo == 'M':
        qtdHomens += 1
        if qtdHomens == 1:
            nomeVelho = nome
            
        else:
            if idade > idadeAnterior:
                nomeVelho = nome
                
        idadeAnterior = idade
    
    if sexo == 'F' and idade < 20:
        mulVinte += 1

media = acumIdade / 4

print(f'\n{"CONCLUSÃO":-^30}')
print(f'MÉDIA DA IDADE DO GRUPO: {media:.2f}')
print(f'NOME DO HOMEM MAIS VELHO: {nomeVelho}')
print(f'Quantidade de mulheres com idade abaixo de 20: {mulVinte}')