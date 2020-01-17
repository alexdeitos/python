lista = []
while True:
    v = int(input("Digite um valor: "))
    if v in lista:
        print("Valor duplicado não adicionado!")
    else:
        lista.append(v)
        print("Valor adicionado com sucesso...")
    op = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    if op == 'N':
        break
print(sorted(lista))