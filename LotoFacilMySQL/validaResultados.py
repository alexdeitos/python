def validadorResultados():
    vetorJogado = []
    qtd_jogos = int(input(f'Digite a quantidade de jogos que deseja validar\n==>'))
    for i in range(0, qtd_jogos):
        numeros = []
        x = 1
        print('#' * 100)
        print('\nDigite os seu jogo\n')
        print('#' * 100)
        while True:
            while True:
                n = int(input(f'Digite o {x}° número do seu jogo {i}: '))
                if n not in numeros and n < 26:
                    numeros.append(n)
                    break
                else:
                    if n > 25:
                        print('valor invalido!')
                    else:
                        print('numero repetido!')
                    continue
            x += 1
            if x == 16:
                vetorJogado.append(numeros[:])
                numeros.clear()
                break
        i += 1
    x = 1
    y = 1
    vetorResultados = []
    print('#' * 100)
    print('\nDigite os sorteados pela caixa\n')
    print('#' * 100)

    while True:
        while True:
            n = int(input(f'Digite o {x}° número sorteado pela caixa: '))
            if n not in vetorResultados and n < 26:
                vetorResultados.append(n)
                break
            else:
                if n > 25:
                    print('valor invalido!')
                else:
                    print('valor repetido!')
                continue
        x += 1
        if x == 16:
            break

    for n in vetorJogado:
        acertos = 0
        for numero in n:
            if numero in vetorResultados:
                acertos += 1
        if acertos == 15:
            print()
            print('#' * 100)
            print(f'\nVocê acertou os {acertos} números no jogo {y}! Parabéns está milhonário!!!\n')
            print('#' * 100)
            print()
        else:
            print()
            print('#' * 100)
            print(f'\nVocê acertou {acertos} números!\n')
            print('#' * 100)
            print()
    y += 1