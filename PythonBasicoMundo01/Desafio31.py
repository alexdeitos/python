"""

Desenvolva um programa que pergunte a distância de uma viagem em Km.
 Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
 e R$0,45 parta viagens mais longas.

"""

km = float(input("Digite a distância da sua viagem: "))
if km >= 200:
    custo = km * 0.45
    print("Sua passagem custará R${:.2f}".format(custo))
else:
    custo = km * 0.50
    print("Sua passagem custará R${:.2f}".format(custo))
