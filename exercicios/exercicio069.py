# Ler sexos e idades
# Perguntar se deseja continuar cadastrando
# Quantas pessoas tem mais de 18
# Quantos homens foram cadastrados
# Quantas mulheres tem menos de 20 anos

resp = 'S'
sexo = idade = None
contPessoas = contAdultos = contM = contF20 = 0

print(f'{"CADASTRO DE PESSOAS":-^25}')
while resp == 'S':
    contPessoas += 1
    print(f'{contPessoas}º PESSOA:')
    sexo = str(input('SEXO: ')).upper()[0]
    idade = int(input('IDADE: '))
    
    print('\n\033[33mANALISANDO...\033[m')
    if idade > 18:
        contAdultos +=1
        print(f'\033[32m- Idade maior que 18✅\033[m')

    if sexo == 'M':
        contM += 1
        print(f'\033[32m- Sexo Masculino✅\033[m')
    if sexo == 'F' and idade < 20:
        contF20 += 1
        print(f'\033[32m- Moça com idade menor a 20 anos✅\033[m')

    resp = str(input('\n\033[33mDESEJA CONTINUAR[S/N] -> \033[m')).upper()[0]
    while resp not in 'SN':
        resp = str(input('Resposta inválida! Deseja continuar[S/N] -> '))

print(f'\n\033[31m{"CONCLUSÃO":-^25}\033[m')
print(f'Quantidade total de pessoas -> {contPessoas}')
print(f'Quantidade de pessoas com mais de 18 anos -> {contAdultos}')
print(f'Quantidade de homens -> {contM}')
print(f'Quantidade de mulheres com menos 20 anos-> {contF20}')