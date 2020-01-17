termo = int(input("Qual o primeiro termo?\n==>"))
razao = int(input("Qual a razao?\n==>"))
decimo_termo = termo + 10 * razao
for c in range(termo,decimo_termo,razao):
    print("{}".format(c), end='-> ')
print("ACABOU!")