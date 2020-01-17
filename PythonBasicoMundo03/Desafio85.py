num = [[],[]]
for x in range(1,8):
    n = int(input(f'Digite o {x}° valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print(f'Números pares digitados: {sorted(num[0])}')
print(f'Números impares digitados: {sorted(num[1])}')



