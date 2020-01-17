'''

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

'''
list = []
mulheres = 0
media_idade = 0
total_idade = 0
maior_idade = 0
nome_mais_velho = ''

for i in range(4): # create a list with nested lists
    list.append([])
    print("-"*5+" {}° PESSOA ".format(i+1)+"-"*5)
    nome = input("Digite o {}° nome:".format(i+1)).strip().upper()
    idade= int(input("Digite a idade da {}° pessoa:".format(i+1)))
    sexo = input("Sexo da {}° pessoa [M / F]:".format(i+1)).strip().upper()

    #ADICIONA PESSOAS A LISTA
    list[i].append(nome)
    list[i].append(idade)
    list[i].append(sexo)

    total_idade += list[i][1]

    # SOMA QUANTIDADE DE MULHERES MAIORES QUE 20 ANOS
    if list[i][1] < 20 and list[i][2] == 'F':
       mulheres += 1

    # VALIDA HOMEM MAIS VELHO
    if list[i][2] == 'M':
       if list[i][1] > maior_idade:
          nome_mais_velho = list[i][0]
          maior_idade = list[i][1]
#CALCULA A MEDIA DE IDADE DE TODAS AS PESSOAS
media_idade = total_idade / len(list)

#IMPRIME O RESULTADO
print("\nA media de idade das pessoas é {:.0f}".format(media_idade))
print("O homem mais velho é o {} com {} anos".format(nome_mais_velho,maior_idade))
print("Tem {} mulher/mulheres com menos de 20 anos".format(mulheres))



