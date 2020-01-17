from random import randint
from time import sleep
jogos = int(input('Quantos jogos quer gerar ? \n=>'))
print('-=' * 3, f'SORTEANDO {jogos} JOGOS','-=' * 3)
listajogos=[]
for x in range(jogos):
    while True:
            i = randint(1,60)
            if i not in listajogos:
               listajogos.append(i)
            else:
                continue
            if len(listajogos) == 6:
                break
    print('...')
    sleep(1.0)
    print(f'Jogo {x+1}: {sorted(listajogos)}')
    listajogos.clear()


