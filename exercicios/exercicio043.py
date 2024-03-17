# Calculando IMC

print(f'{"CALCULANDO IMC":-^20}')
peso = float(input('Qual o peso? '))
altura = float(input('Qual a altura(em metros)? '))

imc = peso / altura**2

print(f"\n{'RESULTADO':-^20}")
print(f'IMC ---> {imc:.2f}')
print('SITUAÇÃO: ', end='')

if imc < 18.5:
    print('{}Abaixo do peso'.format('\033[31;4m'))
elif imc < 25:
    print('{}Peso ideal'.format('\033[32;4m'))
elif imc < 30:
    print('{}Sobrepeso'.format('\033[35;4m'))
elif imc < 40:
    print('{}Obesidade'.format('\033[31;4m'))
else:
    print('{}Thaís Carla'.format('\033[31;44;4m'))
print('\033[m', end='')