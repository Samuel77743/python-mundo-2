# Categoria de Nadador
# Até 9: Mirim | Até 14: Infantil | Até 19: Júnior | Até 20: Sênior
# Acima: MASTER

print(f'{"CATEGORIZANDO":-^20}')

idade = int(input('Qual a idade do nadador -> '))

print('Nadador nível ', end='\033[4m')
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Júnior')
elif idade <= 20:
    print('Sênior')
else:
    print('Master')

print('\033[m')