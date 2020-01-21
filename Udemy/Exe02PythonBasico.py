# receba duas notas do usuário se for 6 ou maior imprima aprovado
# caso seja menor de 6 imprima reprovado

notas = []
for i in range(1,3):
    n = float(input(f"Digite a nota {i}: "))
    notas.append(n)
for n in notas:
    if n >= 6 :
        print(f"Nota {n} aprovado!")
    else:
        print(f"Nota {n} reprovado!")
