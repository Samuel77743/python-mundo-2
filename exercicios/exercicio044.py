#Diferentes modos de pagamentos
valorCompra = float(input('Qual o valor da compra? R$ '))

print(f"""
{"FORMAS DE PAGAMENTO":=^30}
[1] À vista no Dinheiro (10% de Desconto)
[2] À vista no Cartão de Crédito (5% de Desconto)
[3] Em  2x no Crédito (Sem Desconto)
[4] A partir de 3x no Crédito \033[31m(20% de Juros)
\033[m""")

resp = int(input('SUA RESPOSTA -> '))
print() #Quebra de linha

total = None
if resp == 1:
    print(f'{"À VISTA NO DINHEIRO":-^30}')
    desconto = valorCompra*10/100
    total = valorCompra - desconto
elif resp == 2:
    print(f'{"À VISTA NO CARTÃO DE CRÉDITO":-^30}')
    desconto = valorCompra*5/100
    total = valorCompra - desconto
elif resp == 3:
    print(f'{"EM 2x NO CARTÃO DE CRÉDITO":-^30}')
    desconto = 0
    total = valorCompra
    print(f'Duas parcelas de {total/2:.2f}')
else:
    while True:
        print(f'{"A PARTIR DE 3 PARCELAS":-^30}\033[3m')
        qtdParcelas = int(input('Digite em quantas vezes deseja parcelar -> '))
        if qtdParcelas < 3:
            continue
        juros = valorCompra*20/100
        total = valorCompra + juros
        print(f'JUROS: R$ {juros}')
        print(f'{qtdParcelas} parcelas de R$ {total/qtdParcelas:.2f}\033[m')
        desconto = 0
        break

print(f'Valor dos Produtos: R$ {valorCompra:.2f}')
print(f'DESCONTO: R$ {desconto:.2f}')
print(f'TOTAL A SER PAGO: R$ {total:.2f}')
