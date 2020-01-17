from random import randint

def sorteia(lista):
    for x in range(1, 7):
        lista.append(randint(1, 10))
    print(lista)

def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos números pares da lista é {soma}')
numeros = list()
print('Sorteando números:')
sorteia(numeros)
print()
somaPar(numeros)



