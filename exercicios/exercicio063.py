# Algoritmo de Fibonacci

print(f'{"FIBONACCI":-^20}')

print('Quantos termos da sequência de fibonacci deseja imprimir?')
qtdTermos = int(input('SUA RESPOSTA -> '))

cont = 1
seq = [0, 1]

while cont <= qtdTermos - 2:
    seq.append(seq[cont-1]+seq[cont])
    cont += 1

for i in seq:
    print(f'{i} -> ', end='')

