'''

Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

'''
'''
while True:
    valor = int(input("Qual o valor a ser sacado ?"))
    cedula50 = valor // 50
    valor %= 50
    cedula20 = valor // 20
    valor %= 20
    cedula10 = valor // 10
    valor %= 10
    cedula01 = valor // 1
    valor %= 1
    if valor == 0:
        break
if cedula50 != 0 :
    print(f'Serão {cedula50} de R$50')
if cedula20 != 0:
    print(f'Serão {cedula20} de R$20')
if cedula10 !=0:
    print(f'Serão {cedula10} de R$10')
if cedula01 !=0:
    print(f'Serão {cedula01} de R$1')
'''

from random import randint
a = 0
while a < 6:
    x = randint(1,60)
    print(x ,end=' - ')
    a +=1
print("Ta na mão")


