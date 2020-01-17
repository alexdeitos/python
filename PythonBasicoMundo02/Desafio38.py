"""
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
O primeiro valor é maior -
O segundo valor é maior -
Não existe valor maior, os dois são iguais

"""

a = float(input("Digite o primeiro valor:"))
b = float(input("Digite o segundo valor:"))
if a > b:
    print("O primeiro valor é maior")
elif b > a:
    print("O Segundo valor é maior")
else:
    print("Não existe valor maior, os dois são iguais")
