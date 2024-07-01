# Convertendo em BIN

numInt = int(input('Digite o número a ser convertido -> '))
quociente = numInt
digitosBin = []
while quociente >= 1:
    digitosBin.append(quociente%2)
    quociente = quociente//2

numBin = digitosBin[len(digitosBin)-1::-1]
print(f'ORIGINAL: {numInt}\nEM BINÁRIO: {numBin}')