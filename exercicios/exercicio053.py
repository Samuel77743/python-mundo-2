# É palíndromo?

print(f'{"PALÍNDROMO":-^20}')
palavra = input('Digite a palavra -> ')

palavraOp = palavra[len(palavra)-1::-1]

isPalindromo = palavra.upper() == palavraOp.upper()

print(f"""
Original...... {palavra}
Ao contrário.. {palavraOp}""", end='\n\n')

print(f'CONCLUSÃO: {"É PALÍNDROMO" if isPalindromo else "NÃO É PALÍNDROMO"}')
