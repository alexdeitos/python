soma  = 0
cont = 0
for c in range(1,7):
    a = int(input("digite o {}° numero: ".format(c)))
    if a%2==0:
        soma += a
        cont += 1
print("Você informou {} números pares e a soma deles foi {}".format(cont,soma))


