import xlrd

from funcLotoFacil import *

cont = 0
cont1 = 0
cont11 = 0
cont12 = 0
cont13 = 0
cont14 = 0
cont15 = 0

arquivo = xlrd.open_workbook('lotofacil.xlsx')
print(f'Número de abas:{arquivo.nsheets}')
print(f'Nome da planilha: {arquivo.sheet_names()}')
sh = arquivo.sheet_by_index(0)
linhas = sh.nrows
colunas = sh.ncols
jogos = list()
numeros =list()

print(f'O arquivo possui {linhas} linhas e {colunas} colunas!')

for linha in range(0,sh.nrows):
    for coluna in range (2,(sh.ncols-1)):
        numeros.append(int(f'{sh.cell_value(rowx=linha, colx=coluna):.0f}'))
    jogos.append(numeros[:])
    numeros.clear()

qtdJogos = int(input('Quantos Jogos? '))

while True:
        v = gerarNumerosJogos()
        if validandoParametros(v) == True:
            cont1 += 1
            print('=-=-=-=' * 5)
            print(f'Jogo que atende os parametros: {v}')
            print(f'Foram necessarios {cont} jogos!')
            print('=-=-=-=' * 5)
            print()
        cont += 1
        if cont1 == qtdJogos:
            break
print('=-=-=-=' * 5)
print("Finalizado com sucesso!")
print('=-=-=-=' * 5)

