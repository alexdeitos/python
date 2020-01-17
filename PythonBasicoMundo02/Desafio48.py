"""

Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500

"""
soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 ==0:
        soma += c
        cont += 1
print("Entre 1 e 500 existem {} valores multiplos de 3 e a soma deles é {}".format(cont,soma))


