palavraOriginal = input('Escreva a palavra -> ')

p1 = ''.join(palavraOriginal.split(' ')).lower()
p2 = p1[len(p1)::-1].lower()

print(f'Palavra original -> {p1}')
print(f'Palavra ao contrário -> {p2}')

print(f'\nCONCLUSÃO: {"é" if p1 == p2 else "não é"}')