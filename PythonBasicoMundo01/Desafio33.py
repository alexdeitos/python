'''

leia 3 valores
imprima o maior dos 3
imprima o menor dos 3

'''
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if n1 > n2 and n1 > n3:
    maior = n1
if n1 < n2 and n1 < n3:
    menor = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n2 < n1 and n2 < n3:
    menor = n2
if n3 > n2 and n3 > n1:
    maior = n3
if n3 < n2 and n3 < n1:
    menor = n3

print("{} é o maior e o {} é o menor".format(maior,menor))

'''
solução simplificada:

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > a and n3 > n2:
    maior = n3
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
    
'''



