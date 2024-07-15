from datetime import date
# Quantas pessoas são adultas
print(f'{"Filtro de Maioridade":-^25}')

acumMaiores = 0
acumMenores = 0
for i in range(1, 8):
    resp = int(input(f'Digite o {i}º ano de nascimento -> '))
    if date.today().year - resp >= 18:
        print('\033[032mÉ maior👌')
        acumMaiores += 1
    else:
        print('\033[031mNão é Maior❌')
        acumMenores += 1
    print('\033[m', end='')

print(f'Quantidade de Maiores- > {acumMaiores}')
print(f'Quantidade de Menores- > {acumMenores}')

