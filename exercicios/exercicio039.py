# Alistamento Militar

print(f'{"ALISTAMENTO MILITAR":-^26}')

try:
    idade = int(input('Qual a sua idade: '))
except ValueError:
    print('{}Valor inválido!{}'.format('\033[45m', '\033[m'))
    exit()

diferenca = 18 - idade

if idade < 18:
    print('{}Ainda irá se alistar, em {} ano(s){}'.format('\033[33m', diferenca, '\033[m'))

elif idade == 18:
    print('{}É hora de se alistar!{}'.format('\033[32m', '\033[m'))

else:
    print('{}Já passou da hora de alistar, está atrasado {} anos{}'.format('\033[31m', diferenca*-1,  '\033[m'))





