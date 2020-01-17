tempPessoas = []
pessoas = []
maisPesadas = []
maisLeves = []
while True:
    tempPessoas.append(str(input("Digite o nome: ")))
    tempPessoas.append(float(input("Digite o peso: ")))
    pessoas.append(tempPessoas[:]) # cria uma copia de tmpPessoas em pessoas
    tempPessoas.clear() # evita ficar duplicando dados
    opcao = str(input('Deseja continuar [S/N]? '))

    if opcao in 'Nn':
        break

for p in pessoas:
    if p[1] > 65:
        maisPesadas.append(p[0])
    elif p[1] < 65:
        maisLeves.append(p[0])
print(f"Ao todo foram cadastradas {len(pessoas)} pessoas")
print(f'As pessoas mais leves são {maisLeves}')
print(f'As pessoas mais pesadas são {maisPesadas}')