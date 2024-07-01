print(f'{"CALCULANDO IMC":=^25}')

altura = float(input('Qual a sua altura? '))
peso = float(input('Qual a seu peso(Em KG)? '))

# IMC é o peso divido pela altura elevado a 2
imc = peso / altura**2
print(f'SEU IMC: {imc:.2f}')

print('Sua situação:', end=' ')
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
    print('\033[31mCUIDADO!\033[m')



