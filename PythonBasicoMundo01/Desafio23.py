"""
faça um programa que leia um número
EX: 1879
e mostre:
unidade: 9
dezena: 7
centena:8
milhar: 1

"""

num = int(input("Digite um numero"))
unidade = num  // 1 % 10
dezena  =  num // 10 % 10
centena = num  // 100 % 10
milhar  =  num // 1000 % 10

print("Unidade: {}".format(unidade))
print("Dezena : {}".format(dezena))
print("Centena: {}".format(centena))
print("Milhar : {}".format(milhar))
