# Qual maior/menor valor (ou se é Igual)

print(f'{"TESTE":-^20}')
num1 = int(input('Digite o 1º número -> '))
num2 = int(input('Digite o 2º número -> '))

if num1 == num2:
    print('{}O 1º e 2º número são iguais!{}'.format('\033[33m', '\033[m'))
elif num1 > num2:
    print('{}O 1º é maior que o 2º número{}'.format('\033[32m', '\033[m'))
else:
    print('{}O 2º é maior que o 1º número{}'.format('\033[31m', '\033[m'))