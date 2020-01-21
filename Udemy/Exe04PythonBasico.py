# ordenação de lista

lista = []
for i in range(1,4):
    lista.append(int(input(f"Digite o valor {i}: ")))
print(sorted(lista))