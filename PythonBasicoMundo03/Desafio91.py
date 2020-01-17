from random import randint
from time import sleep
from operator import itemgetter
jogador = {'Jogador 1':'','Jogador 2':'','Jogador 3':'','Jogador 4':''}
print('-='* 30)
print(f"{'GERANDO JOGOS':^60}")
print('-=' * 30)
for x in range(1,5):
    jogador[f'Jogador {x}'] = randint(1, 6)
    print(f"O Jogador {x} tirou {jogador[f'Jogador {x}']}",end=' ...\n' if x < 4 else ' ')
    sleep(1.0)
print()
ranking = sorted(jogador.items(), key = itemgetter(1),reverse=True)
print('-='* 30)
print(f"{'RESULTADO DOS JOGOS FORAM':^60}")
print('-=' * 30)
for v, k in enumerate(ranking):
    print(f'{f"{v+1}° Lugar: {k[0]} com {k[1]} pontos!":^60}')
    sleep(1)
print('-='* 30)
print(f"{'FIM DE JOGO E VOLTE SEMPRE!':^60}")
print('-=' * 30)






