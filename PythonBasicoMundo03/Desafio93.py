jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas ele jogou: '))
jogador['gols'] = []
jogador['total'] = 0
for x in range(0,partidas):
    jogador['gols'].append(int(input(f'   Quantos gols na partida {x+1}?  ')))
    jogador['total'] += jogador['gols'][x]
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas:")
for x in range(len(jogador['gols'])):
    print(f'   => Na partida {x+1} o jogador {jogador["nome"]} fez {jogador["gols"][x]} gols. ')
print(f"Foi um total de {jogador['total']} gols.")
