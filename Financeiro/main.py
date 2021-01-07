jump2 = "\n" * 2
print(100 * "#")
print(25 * "#", end="")
print(f"{'Sistema de Controle Financeiro Pessoal':^50}", end="")
print(25 * "#")
print(100 * "#")
print(jump2)
while True:
    try:
        print("[1] - Opção 1")
        print("[2] - Opção 2")
        print("[3] - Opção 3")
        print("[4] - Opção 4")
        print("[5] - Opção 5\n")
        option = int(input("Digite a opção desejada:"))
    except (ValueError, TypeError):
        print('*' * 30)
        print(f"\n{'Digite apenas números':^30}\n")
        print('*' * 30)
        continue
    else:
        print(jump2)
        print("é nóis que voa, manda a função aqui")
        print(jump2)
        break

