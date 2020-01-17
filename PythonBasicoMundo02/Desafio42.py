'''

Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.

condição:

| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b

'''

n1 = float(input("Digite o primeiro segmento: "))
n2 = float(input("Digite o segundo segmento: "))
n3 = float(input("Digite o terceiro segmento: "))

sit1 = (n2 - n3) < n1 < n2 + n3
sit2 = (n1 - n3) < n2 < n1 + n3
sit3 = (n1 - n2) < n3 < n1 + n2

if(sit1 and sit2 and sit3):
    if n1 == n2 == n3:
        print("As 3 medidas formam um triângulo EQUILÁTERO!")
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print("As medidas formam um triângulo ISÓSCELES!")
    else:
        print("As medidas formam um triângulo ESCALENO!")
else:
    print("Segmentos não formam um triangulo!")

