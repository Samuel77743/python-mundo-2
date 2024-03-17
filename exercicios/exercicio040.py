# Média e Situação do aluno

print(f'{"CALCULANDO MÉDIA":=^20}')

qnt = int(input('Quantas provas o aluno fez -> '))
i = 1
acum = 0

while i <= qnt:
    acum += float(input(f'Qual a nota do aluno na {i}º prova? '))
    i+=1

media = acum / qnt
print(f'{"SITUAÇÃO":=^20}')
print(f'NOTA DO ALUNO: {media}')
print('STATUS: ', end='')

if media < 5:
    print('{}REPROVADO{}'.format('\033[41m', '\033[m'))
elif media < 7:
    print('{}RECUPERAÇÃO{}'.format('\033[43m', '\033[m'))
else:
    print('{}APROVADO{}'.format('\033[42m', '\033[m'))