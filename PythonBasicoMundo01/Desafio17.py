""" Leia o cateto oposto e o cateto adjacente de um triangulo retangulo e calcule e mostre
o comprimento da hipotenusa """

# hipotenusa elevado ao quadrado é igual a soma dos quadrados dos outros dois lados

from math import hypot

co = float(input("Digite o valor do cateto oposto:"))
ca = float(input("Digite o valor do cateto adjacente:"))

def hipotenusa(co, ca):
    return hypot(co,ca)

print("A medida da hipotenusa é de {:.2f}".format(hipotenusa(co,ca)))

