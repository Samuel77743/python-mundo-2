#CLASSIFICAÇÃO DO ATLETA
from datetime import date 
print(f'{"CLASSIFICAÇÃO DE ATLETA":=^30}')

anoNascimento = int(input('Qual o ano de nascimento: '))
idade =  date.today().year - anoNascimento

print('\nCLASSIFICAÇÃO: ', end='')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')