def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato!')

nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Quantidade de gols: ')).strip()

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome == '':
    ficha(gol=gols)
else:
    ficha(nome,gols)