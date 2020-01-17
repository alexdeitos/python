'''

Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

'''
pesos = []
for c in range(1, 6):
    peso = float(input("Digite o peso da {}° pessoa:".format(c)))
    pesos.append(peso)
print("O {} foi o menor peso e {} foi o maior".format(min(pesos),max(pesos)))