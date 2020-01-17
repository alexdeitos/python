lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    op = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if op == 'N':
        break
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem descrescente são {sorted(lista,reverse=True)}')
print(f'O número 5 {"foi" if 5 in lista else "não foi"} adicionado a lista.')


