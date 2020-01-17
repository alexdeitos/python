from random import randint

def gerarNumerosJogos():

    '''valores da lista A'''
    vetorA = []

    '''Gerando números aleatórios no vetor A sem repetição'''
    x=0
    while True:
        numAleatorioA = randint(1,25)
        if numAleatorioA not in vetorA:
            vetorA.append(numAleatorioA)
            x +=1
        if x == 15:
            break
    vetorA = sorted(vetorA)
    return vetorA


def validandoParametros(jogoGerado):

    contFracas = contImpar = contPar = contFibo = contPrimo = contMultiplos = contFortes = contMoldura = soma = contFixa = 0
    vetorFibonacci = [1, 2, 3, 5, 8, 13, 21]
    vetorPrimos = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    vetorMultiplos = [3, 6, 9, 12, 15, 18, 21, 24]
    vetorNumFortes = [5,6,7,12,13,14,19,20,21]
    vetorMoldura = [1, 2, 3, 4, 5, 6, 10, 11, 15, 16, 20, 21, 22, 23, 24, 25];
    vetorFracas  = [2,5,11,13,15]
    valida = False

    for n in jogoGerado:
        soma += n

        if n % 2 != 0:
            contImpar += 1
        else:
            contPar += 1
        if n in vetorFibonacci:
            contFibo += 1
        if n in vetorPrimos:
            contPrimo += 1
        if n in vetorMultiplos:
            contMultiplos += 1
        if n in vetorNumFortes:
            contFortes += 1
        if n in vetorMoldura:
            contMoldura += 1
        if n in vetorFracas:
            contFracas += 1

    if  contImpar == 11 and 3 <= contFibo <= 4 and 4 <= contMultiplos <= 7 and 4 <= contPrimo <= 5 and contFortes == 9\
       and 1 <= contFracas <= 2 and 9 <= contMoldura <= 11:
           valida = True
    return valida














