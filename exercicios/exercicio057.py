# Interrogatório em LOOP
print(f'{"PERGUNTA EM LOOP":-^20}')
resp = ''

while resp not in ['M', 'F']:
    resp = str(input('DIGITE SEU SEXO [M/F] -> ')).upper()

print('Sexo Masculino!' if resp == 'M' else 'Sexo feminino!')