# Total da compra
# Quantos custam mais que 1000
# Nome e preço do produto mais barato

print(f'{"":-^25}')
print(f'{" LOJA BARATÃO ":-^25}')
print(f'{"":-^25}')

nome = preco = None
cont = mais1000 = total = 0
resp = 'S'

while resp == 'S':
    nome = str(input('Nome do Produto........ '))
    preco = float(input('VALOR DO PRODUTO....... R$ '))
    cont += 1

    # Total
    total += preco

    # Obtendo mais barato
    if cont == 1:
        maisBaratoNome = nome 
        maisBaratoPreco = preco
    elif preco < maisBaratoPreco:
        maisBaratoNome = nome
        maisBaratoPreco = preco

    # Quantos custam mais que 1000
    if preco > 1000:
        mais1000 += 1

    # Deseja tentar novamente?
    resp = str(input('Deseja continuar[S/N] -> ')).upper()[0]
    while resp not in 'SN':
        print('Resposta inválida! Tente novamente')
        resp = input('SUA RESPOSTA -> ')

print(f'\n{"CONCLUSÃO":-^25}')
print(f"""
TOTAL DA COMPRA..................... R$ {total:,.2f}
QTD. QUE CUSTAM MAIS QUE 1000....... {mais1000}
PRODUTO MAIS BARATO................. {maisBaratoNome} custando R$ {maisBaratoPreco:,.2f}""")