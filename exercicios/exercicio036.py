#Programa de Empréstimo para adquirir casa
# Perguntas: 
# 1 - Valor da Casa
# 2 - Salário do cliente
# 3 - Em quantos ANOS irá pagar
# DETALHE: SERÁ NEGADO CASO CADA PARCELA CUSTE MAIS QUE 30% DO SALÁRIO

print(f"{'EMPRÉSTIMO':-^20}")
salarioCliente = float(input("Digite seu salário: R$ "))
emprestimoTotal = float(input("Qual o valor da casa: R$ "))
anos = int(input("Em quantas anos pretende pagar: "))
valorParcela = emprestimoTotal/(anos*12)
print(f"Totalizando R$ {valorParcela:.2f} por parcela...")

if(valorParcela <= 30/100*salarioCliente):
    print("\033[32m")
    print("Empréstimo concedido!")
else:
    print("\033[31m")
    print("Empréstimo negado!")
    print("\033[30;43m")
    print(
    f"""Valor mínimo: R$ {30/100*salarioCliente:.2f},
restou ter R$ {valorParcela-30/100*salarioCliente:.2f} por mês""", end='')  

print("\033[m")