from random import randint
from LotoFacilMySQL.connect_mysql import conecta

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

def validandoParametros(jogoGerado,result,minImpar,maxImpar,minRep,maxRep,minPrimo,maxPrimo,minMold,maxMold,
                        minFibo,maxFibo,minMult,maxMult):
    # Vetores:
    vetorPrimos = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    vetorMoldura = [1, 2, 3, 4, 5, 6, 10, 11, 15, 16, 20, 21, 22, 23, 24, 25]
    vetorMultiplos = [3, 6, 9, 12, 15, 18, 21, 24]
    vetorFibonacci = [2, 3, 5, 8, 13, 21]
    # Contadores:
    contPrimo = contMoldura = contRepetidas = soma = contImpar = contMultiplos = contFibonacci =0
    valida = False
    for n in jogoGerado:
        soma += n
        if n % 2 != 0:
            contImpar += 1
        if n in vetorPrimos:
            contPrimo += 1
        if n in vetorMoldura:
            contMoldura += 1
        if n in result[0]:
            contRepetidas += 1
        if n in vetorMultiplos:
            contMultiplos += 1
        if n in vetorFibonacci:
            contFibonacci += 1
    # Caso atenda os padrões a seguir retorna verdadeiro para o jogo
    if minImpar <= contImpar <= maxImpar and minPrimo <= contPrimo <= maxPrimo and minRep <= contRepetidas <= maxRep \
        and minMold <= contMoldura <= maxMold and minFibo <= contFibonacci <= maxFibo and \
        minMult <= contMultiplos <= maxMult and 180 <= soma <= 208:
        valida = True
    return valida

def validaResultadosJogoGerado(game):
    mydb = conecta()
    mycursor = mydb.cursor()
    jogos_bd = []
    jg  = []
    acertou = 0
    acertos = []
    onze = 0
    doze = 0
    treze = 0
    quatorze = 0
    quinze = 0
    sql = "select * from jogos"
    mycursor.execute(sql)
    resultado = mycursor.fetchall()
    for j in resultado:
        for i in range(1,16):
            #print(j[i], end=' ')
            jg.append(j[i])
        jogos_bd.append(jg[:])
        jg.clear()
    for jogo in jogos_bd:
        for n in jogo:
            if n in game:
               acertou += 1
        acertos.append(acertou)
        acertou = 0
    for ac in acertos:
        if ac == 11:
            onze += 1
        elif ac == 12:
            doze += 1
        elif ac == 13:
            treze += 1
        elif ac == 14:
            quatorze += 1
        elif ac == 15:
            quinze += 1

    return (f"\nAcertos obtidos com o jogo gerado na história da lotofácil:\n"
                   f"11 pontos: {onze}\n12 pontos: {doze}\n13 pontos: {treze}\n14 pontos: {quatorze}\n15 pontos: {quinze}\n")
