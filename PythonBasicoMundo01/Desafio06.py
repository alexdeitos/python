#Leia um número mostre o dobro o triplo e a raiz quadrada

from math import sqrt
num = int(input("Digite um numero: "))
d = num * 2
t = num * 3
r = sqrt(num) # tambem pode ser r = num ** (1/2)

print(" Dobro : {} \n Triplo: {} \n Raiz Quadrada: {:.2f}".format(d,t,r))