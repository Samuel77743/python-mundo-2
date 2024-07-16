#Digite valores enquanto quiser
# Informar qtd, soma, média, maior e menor
cont = acum = 0
num = maior = menor = None
resp = 'S'
while resp == 'S':
    num = int(input('Digite um número -> '))
    acum += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Deseja digitar novamente?[S/N] ')).upper().strip()[0]

media = acum / cont
print(f'\n{"CONCLUSÃO":-^25}')
print(f'Quantidade de números digitados: {cont}')
print(f'Soma dos números digitados: {acum}')
print(f'Média dos números digitados: {media}')
print(f'Maior dos números digitados: {maior}')
print(f'Menor dos números digitados: {menor}')
            
