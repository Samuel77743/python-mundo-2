# EMPRÉSTIMO BANCÁRIO
# O Cliente tentará comprar uma casa

print(f'{"EMPRÉSTIMO BANCÁRIO":-^25}')

valorCasa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o salário? R$ '))
anos = int(input('Em quantos anos será pago o valor -> '))
# Anos em meses
meses = anos*12
prestacao = valorCasa/meses

print(f'\n{"NOTA":-^25}')
print(f'VALOR DO EMPRÉSTIMO ---> R$ {valorCasa:.2f}')
print(f'MENSALIDADE ---> {meses} ({anos} anos)')
print(f'Salário do cliente ---> R${salario:.2f}')

salarioExigido = 30/100 * prestacao
print(f'\n{"CONCLUSÃO":=^25}')

if salario >= salarioExigido:
    print('EMPRÉSTIMO {}APROVADO{}'.format('\033[32;4m', '\033[m'))
else:
    print('EMPRÉSTIMO {}REPROVADO{}'.format('\033[31;4m', '\033[m'))
