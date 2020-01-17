def area(l, c):
    a = l * c
    print(f'A área do terreno {l} x {c} é de {a}m²')


print('Controle de Terrenos')
print('-' * 20)
area(float(input('Largura (m): ')),float(input('Comprimento (m): ')))

