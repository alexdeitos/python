cont = soma = 0
while True:
    n = int(input("Digite um valor: [999 para sair]\n==>"))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} valores e a soma entre eles é de {soma}')