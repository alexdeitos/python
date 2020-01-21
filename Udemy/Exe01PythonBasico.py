# receba uma idade e diga se é de maior ou de menor

while True:
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        print("\n\nJá atingiu a maior idade!\n\n")
    else:
        print("\n\nAinda é menor de idade!\n\n")
    op = int(input("Deseja continuar?\n 1 - SIM\n 2 - NÂO \n--> "))
    if op == 2:
        print("Execução finalizada!")
        break

