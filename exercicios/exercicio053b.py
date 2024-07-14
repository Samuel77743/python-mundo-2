palavra = input('Qual a palavra -> ')
aux = palavra[len(palavra)-1::-1]
palavraOp = ''

for i in palavra.split():
    palavraOp = palavraOp + i

palavraOp = palavraOp[len(palavraOp)::-1]

print(f"""
PALAVRA ORIGINAL -> {palavra}
PALAVRA OPOSTA -> {aux}
"""
)

isPalindromo = ''.join(palavra.split(' ')).upper() == palavraOp.upper()
print('É PALÍNDROMO' if isPalindromo else 'NÃO É PALÍNDROMO')