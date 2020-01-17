n = resultado = cont = 0
while n != 999:
    n = int(input("Digite o valor: [999 para finalizar]: "))
    if n != 999:
        resultado += n
        cont +=1
print("Finalizado! A soma dos {} valores digitados foi de {}".format(cont,resultado))
