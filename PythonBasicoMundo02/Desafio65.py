resposta = 'S'
cont = media = soma = maior = menor = 0
while resposta in 'Ss':
        n = int(input("Digite um número: "))
        soma += n
        cont += 1
        if cont == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        resposta = str(input("Deseja continuar:[S / N] ")).upper().strip()[0]
media = soma / cont
print(f'Você digitou {cont} valores')
print("Maior valor foi {}".format(maior))
print("Menor valor foi {}".format(menor))
print("Media dos valores digitados foi {}".format(media))