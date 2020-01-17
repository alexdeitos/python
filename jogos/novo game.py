from random import randint

jogo = []


def gera():
    while True:
        a = randint(1,60)
        if a not in jogo:
            jogo.append(a)
        if len(jogo) >= 6:
            break
    return jogo


def valida(jogo):
    superior = inferior = 0
    valido = False

    while True:
        for i in jogo:
            if i <= 30:
                superior += 1
            else:
                inferior += 1
        if superior == 2 and inferior == 4:
            valido = True
            break

    return valido


count = 0
while True:
    count += 1
    jogo = gera()
    if valida(jogo) == True:
        print(f'após {count} jogos foi gerado um que atende os requisitos {jogo}')
        break
    else:
        print(jogo)
