from jogos.gerajogo import *
c = 0
jogos = int(input('\nDeseja gerar quantos Jogos: '))
for i in range(jogos):
    while True:
        c += 1
        j = geraJogoMegaSena()
        if validaMega(j):
            break
    print('-=' * 30)
    print(f'Foram necessários {c} jogos para o resultado:\n {sorted(j)}')

