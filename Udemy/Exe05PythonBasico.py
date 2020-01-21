# receba dois valores e um sinal e imprima a operação dos valores usando o sinal passado


sinal = str(input("Digite o sinal: "))
valor1 = int(input("Digite o valor 1: "))
valor2 = int(input("Digite o valor 2: "))

if sinal == '+':
    resultado = valor1 + valor2
    print("soma: ", resultado)
if sinal == '-':
    resultado = valor1 - valor2
    print("subtração: ", resultado)
if sinal == '/':
    resultado = valor1 / valor2
    print("divisao: ", resultado)
if sinal == '*':
    resultado = valor1 * valor2
    print("multiplicação: ", resultado)
