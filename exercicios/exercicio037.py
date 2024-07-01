#Convertendo bases numéricas

numero = int(input('Qual o número? '))

while(True):
    print("""
    [1] BINÁRIO
    [2] HEXADECIMAL
    [3] OCTAL"""
    )

    resp = int(input('\nSUA RESPOSTA -> '))
    if resp <= 3 and resp > 0: break

if resp == 1:
    numConv = bin(numero).strip("0b")
    print(f'{numero} em BINÁRIO é: {numConv}')
elif resp == 2:
    numConv = hex(numero).strip('0x')
    print(f'{numero} em HEXADECIMAL é: {numConv}')
else:
    numConv = bin(  numero).lstrip('0o')
    print(f'{numero} em OCTAL é: {numConv}')
