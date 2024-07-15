#Digite valores enquanto quiser
# Informar qtd, soma, média, maior e menor
cont = acum = 0
num = maior = menor = None
resp = 'S'
while resp != 'N':

    if cont == 0:
        acum += int(input('Digite um número -> '))
        maior = menor = acum
        cont += 1
    else:
        resp = str(input('Deseja digitar mais um número[S/N] -> ')).upper()[0]
        while resp not in ['S', 'N']:
            resp = str(input('Resposta Inválida! Tente novamente: ')).upper()[0]
        if resp == 'S':
            num = int(input('Digite um número -> '))
            acum += num
            cont += 1
            if num > maior:
                maior = num
                continue
            if num < menor:
                menor = num

media = acum / cont
print(f'\n{"CONCLUSÃO":-^25}')
print(f'Quantidade de números digitados: {cont}')
print(f'Soma dos números digitados: {acum}')
print(f'Média dos números digitados: {media}')
print(f'Maior dos números digitados: {maior}')
print(f'Menor dos números digitados: {menor}')
            
