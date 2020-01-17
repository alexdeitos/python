from random import randint

def gerarNumerosJogos():
    """ valores da lista A """
    vetorA = []
    """ Gerando números aleatórios no vetor A sem repetição """
    x = 0
    while True:
        numAleatorioA = randint(1, 25)
        if numAleatorioA not in vetorA:
            vetorA.append(numAleatorioA)
            x += 1
        if x == 15:
            break
    vetorA = sorted(vetorA)
    return vetorA

def validandoParametros(jogoGerado):
    # Vetores:
    vetorFibonacci = [1, 2, 3, 5, 8, 13, 21]
    vetorPrimos = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    vetorMultiplos = [3, 6, 9, 12, 15, 18, 21, 24]
    vetorMoldura = [1, 2, 3, 4, 5, 6, 10, 11, 15, 16, 20, 21, 22, 23, 24, 25]
    repetidas = [14,3,17,10,1,21,24,4,19,15,16,5,23,18,25]

    # Contadores:
    contFibo = contPrimo = contMultiplos = contMoldura = contRepetidas = soma = contImpar = 0
    valida = False

    for n in jogoGerado:
        soma += n
        if n % 2 != 0:
            contImpar += 1
        if n in vetorFibonacci:
            contFibo += 1
        if n in vetorPrimos:
            contPrimo += 1
        if n in vetorMultiplos:
            contMultiplos += 1
        if n in vetorMoldura:
            contMoldura += 1
        if n in repetidas:
            contRepetidas += 1

    if 7 <= contImpar <= 8 and 4 <= contPrimo <= 6 and 9 <= contRepetidas <= 10 and 4 <= contFibo <= 5\
        and 9 <= contMoldura <= 10 and 4 <= contMultiplos <= 6 and 180 <= soma <= 215:
        valida = True

    return valida
