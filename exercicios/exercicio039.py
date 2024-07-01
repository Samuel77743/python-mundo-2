# Alistamento Militar
from datetime import date

print(f'{"ALISTAMENTO MILITAR":-^25}')
anoAtual = date.today().year

anoNascimento = int(input('Informe o ano de nascimento -> '))
dataAlistamento = anoNascimento + 18

print(f'Quem nasceu em {anoNascimento} tem {anoAtual - anoNascimento} anos de idade atualmente em {anoAtual}')

if dataAlistamento == anoAtual:
    print(f'O alistamento é este ano, de {dataAlistamento}.')
else:
    print(f'O alistamento {"será" if dataAlistamento > anoAtual else "foi"} no ano de {dataAlistamento}')