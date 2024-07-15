
resp = int(input('Qual o número -> '))
cont = resp
resultado = 1

print(f'{resp}! ->', end=' ')
while cont >= 1:
    resultado *= cont
    print(f'{cont} {"x" if cont != 1 else "="}',end=' ')    
    cont -= 1

print(resultado)