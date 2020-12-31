def geraJogoMegaSena():
    import random
    dezenas = [1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 16, 17, 18, 19, 20, 23, 24, 27, 28, 29, 30,
               31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 56, 58, 59]
    # dezenas = [10, 5, 53, 4, 23, 54, 33, 24, 51]

    x = 0
    jogo = []

    while True:
        n = random.choice(dezenas)
        # n = random.randint(1,60)
        if x == 0 or n not in jogo:
            jogo.append(n)
            x += 1
        if x >= 6:
            break
    return jogo


def validaMega(jogo):
    # contadores
    soma = contPar = contQnt = contQdt1 = contQdt2 = contQdt3 = contQdt4 = contBorda = contN = 0
    superior = inferior = 0
    # parametros
    quentes = [10, 5, 53, 4, 23, 54, 33, 24, 51, 17]
    qdt1 = [1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 21, 22, 23, 24, 25]
    qdt2 = [6, 7, 8, 9, 10, 16, 17, 18, 19, 20, 26, 27, 28, 29, 30]
    qdt3 = [31, 32, 33, 34, 5, 41, 42, 43, 44, 45, 51, 52, 53, 54, 55]
    qdt4 = [36, 37, 38, 39, 40, 46, 47, 48, 49, 50, 56, 57, 58, 59, 60]
    borda = [1, 11, 21, 31, 41, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 20, 30, 40, 50, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # booleano validação
    valida = False

    for n in jogo:
        soma += n
        if n % 2 == 0:
            contPar += 1
        if n in quentes:
            contQnt += 1
        if n in qdt1:
            contQdt1 += 1
        if n in qdt2:
            contQdt2 += 1
        if n in qdt3:
            contQdt3 += 1
        if n in qdt4:
            contQdt4 += 1
        if n in borda:
            contBorda += 1
        if n <= 30:
            superior += 1
        if 5 <= n <= 55:
            contN += 1
        else:
            inferior += 1

        if contPar >= 3 and contQnt >= 3 and contQdt1 <= 3 and contQdt2 <= 3 and contQdt3 <= 3 and contQdt4 <= 3 \
                and 100 <= soma <= 200 and contN == 6:
            print(f'\nParametros atendidos!\nPares:{contPar}\nQuentes:{contQnt}\nQuadrante01: {contQdt1}'
                 f'\nQuadrante02: {contQdt2}\nQuadrante03: {contQdt3}\nQuadrante04: {contQdt4}'
                f'\nSoma:{soma}\nBordas:{contBorda}\n')
            valida = True
    return valida

