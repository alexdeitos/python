"""
Leia nome completo de uma pessoa e imprima o primeiro e o ultimo nome
EX:
ana paula

primeiro = ana
segundo  = paula
"""

nome = input("Digite seu nome completo: ")
div = nome.split()
x = len(div)
print("Seu nome completo é {} e seu primeiro nome é {} e seu último nome é {}".format(nome,div[0],div[x-1]))

