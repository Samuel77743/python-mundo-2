# Calculando valor a ser pago
# Envolvendo vários critérios que ocasionam diferentes descontos

# A vista dinheiro ou cheque ->  10% de desconto
# A vista no cartão de débito -> 5% de desconto

# Em até 2x no cartão de crédito -> Preço normal
# 3x ou mais -> 25% de juros

print(f'{"PAGANDO PRODUTO":-^30}')
print(f"{'DIGITE O VALOR':-^20}")
valor = float(input('SUA RESPOSTA -> R$ '))

print(f'\n{"FORMA DE PAGAMENTO":=^30}')
print('[1] Pagamento a vista no dinheiro')
print('[2] Pagamento a vista no cheque')
print('[3] Pagamento por {}CARTÃO{}'.format('\033[4;31m', '\033[m'))

resp = int(input('SUA RESPOSTA -> '))

if resp == 1 or resp == 2:
    valorFinal = valor - valor * 10/100
elif resp == 3:
    print(f'\n{"PAGAMENTO POR CARTÃO":-^30}')
    print('[1] DÉBITO')
    print('[2] CRÉDITO')
    resp = int(input('SUA RESPOSTA -> '))

    if resp == 1:
        valorFinal = valor - valor * 5/100
    elif resp == 2:
        resp = int(input('Será dividido em quantas parcelas? '))
        if resp <= 2:
            valorFinal = valor
        else:
            valorFinal = valor + valor * 25/100
            print(f'\033[31m {"JUROS APLICADO":-^25} \033[m')
            print(f'VALOR DO JUROS ---> {valor + valor * 25/100}')
        print(f'{"AVISO":-^30}')
        print(f'VALOR DE CADA PARCELA -> R$ {valorFinal/resp:.2f}')
else:
    print('Resposta inválida')
    exit()

print(f'\n{"CONCLUSÃO":-^30}')
print(f'Valor Original -------> R$ {valor:.2f}')
print(f'Valor do Desconto ----> R$ {valor - valorFinal:.2f}')
print(f'\nVALOR A PAGAR ------> R$ {valorFinal:.2f}')