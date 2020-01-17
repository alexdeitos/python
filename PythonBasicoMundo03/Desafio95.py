jogadores=[]
jogador = {}
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas ele jogou: '))
    jogador['gols'] = []
    jogador['total'] = 0
    for x in range(0,partidas):
        jogador['gols'].append(int(input(f'   Quantos gols na partida {x+1}?  ')))
        jogador['total'] += jogador['gols'][x]
    jogadores.append(jogador.copy())
    while True:
        op = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        if op in 'SN':
            break
        print('Opção inválida!')
    if op =='N':
        break
print('-=-=-=-' * 10)
print(f'{"Cod.":<5}{"Jogador":<11}{"gols":^15}{"total":^15}')
for k,v in enumerate(jogadores):
    print(f'{k:<5} ',end='')
    for i,dados in v.items():
        print(f'{str(dados):<15}',end='')
    print()
print('-=-=-=-' * 10)
while True:
    j = int(input('Deseja ver os dados de qual jogador [999 para sair]: '))
    if j == 999:
       break
    if j >= len(jogadores):
        print('JOGADOR NÃO CADASTRADO')
    for k, v in enumerate(jogadores):
        if j == k:
            print(f'LEVAMTAMENTO DE DADOS DO JOGADOR {jogadores[k]["nome"]}')
            for x in range(len(jogadores[k]['gols'])):
                print(f'   => Na partida {x + 1} o jogador {v["nome"]} fez {jogadores[k]["gols"][x]} gols. ')
            print(f"Foi um total de {jogadores[k]['total']} gols.")
    print('-=' * 30)






