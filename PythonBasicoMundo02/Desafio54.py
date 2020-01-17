'''

Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

'''
from datetime import date
maior = 0
for c in range(1,8):
    ano = int(input("Ano de nascimento da {}° pessoa: ".format(c)))
    if date.today().year - ano > 21:
        maior += 1
print("Validado que {} são maiores de idade!".format(maior))
print("Validado que {} são menores de idade!".format(7-maior))


