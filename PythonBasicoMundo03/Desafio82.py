lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    op = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if op == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 != 0:
        impares.append(v)
print(f'Lista dos números digitados é {lista}')
print(f'Lista dos números pares digitados foi {pares}')
print(f'Lista dos números impares digitados foi {impares}')

