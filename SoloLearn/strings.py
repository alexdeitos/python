lista = []
for c in range(0, 5):
    n1 = int(input(f'Digite um numero para a posição {c}: '))
    lista.append(n1)
print(f"""O maior numero desta lista foi {max(lista)} e a posição dele na lista foi {lista.index(max(lista))} 
    O menor numero desta lista foi {min(lista)} e a posição dele na lista foi {lista.index(min(lista))}""")