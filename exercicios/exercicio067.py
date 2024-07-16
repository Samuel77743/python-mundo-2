#


while True:
    resp = int(input('Quer ver a tabuada de qual valor? '))
    print('~'*20)
    if resp < 0:
        break
    
    for i in range(1, 11):
        print(f'{resp:2d} x {i:2d} = {resp * i}')
    
    print('~'*20)

print('\n\033[31mPrograma encerrado\033[m')