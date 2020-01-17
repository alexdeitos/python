#declaração de uma lista
pessoas = list()
#declaração de um dicionário
cadastro = dict()
media = 0
#Início do loop para cadastrar pessoas
while True:

    #Limpa o cadastro para uma nova pessoa
    cadastro.clear()

    #inicio de um novo cadastro
    cadastro['nome'] = str(input('Nome: ')).strip()

    #Valida uma entrada válida para sexo
    while True:
        cadastro['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if cadastro['sexo'] in 'FM':
            break
        print('ERRO! Digite apenas M ou F!')

    cadastro['idade'] = int(input('Idade: '))
    media += cadastro['idade']

    #Passa para lista pessoas uma copia do cadastro
    pessoas.append(cadastro.copy())

    #Valida uma entrada válida para oção
    while True:
        op = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if op in 'SN':
            break
        print('ERRO! Digite apenas S ou N!')

    #sai do loop de cadastro de pessoas, caso usuário digite não (N)
    if op == 'N':
        break

#Calculo da media de idade das pessoas cadastradas
media = media/len(pessoas)

print('=-' * 30 )

#Faz a contagem de quantas pessoas foram cadastradas
print(f'Foram cadastradas {len(pessoas)} pessoas.')

#Mostra a média de idade entre as pessoas cadastradas
print(f'A média de idade das pessoas cadastradas é de {media:5.2f}.')

#Lista as mulheres cadastradas
print('As mulheres cadastradas foram')
for p in pessoas:
    if p['sexo'] == 'F':
        print(p['nome'])

#Lista as pessoas cadastradas com a idade acima da média
print('As pessoas cadastradas com idade acima da média são: ')
for p in pessoas:
    if p['idade'] > media:
        print('     ',end='')
        for k,v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<<< ENCERRADO >>>')