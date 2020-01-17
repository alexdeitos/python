"""
matriz = [[],[],[]]
soma = soma3 = maior = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha].append(int(input(f"Digite um valor para a posição [{linha},{coluna}]: ")))
print("-=" * 30)
print(f"{'Matriz':^30}")
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
    print()

        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]
        if linha == 1 and coluna == 0 :
            maior = matriz[linha][coluna]
        elif matriz[1][coluna] > maior:
            maior = matriz[1][coluna]
        if coluna == 2:
            soma3 += matriz[linha][coluna]
"""

print("-=" * 30)
#print(f"A soma dos valores pares é {soma}")
#print(f'A soma dos valores da terceira coluna é {soma3}')
#print(f'Maior valor da segunda linha é {maior}')

matriz=list()
x = 0
while x < 25:
    matriz.append('x')
    x += 1

for x in matriz:
    print(x, end= ' ')
print()
for i in range(0, 15):
    valor = str(input('digite um valor: '))
    print(i)
    if valor is not None:
        matriz[i] = valor


for x in matriz:
    print(f'{x}', end=' - ' if x==25 else ' ')

