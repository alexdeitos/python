lista = []
for c in range(0,5):
    lista.append(int(input(f"digite um número para posição {c}: ")))
print(f"Valores digitados foram: {lista}")
print(f'O maior valor digitado foi {max(lista)} nas posições' , end=' ')
for c,v in enumerate(lista):
    if v == max(lista):
        print(f'{c}...',end=' ')
print(f'\nO menor valor digitado foi {min(lista)} nas posições',end=' ')
for c , v in enumerate(lista):
    if v == min(lista):
        print(f'{c}...')





