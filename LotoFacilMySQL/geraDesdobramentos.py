from LotoFacilMySQL.connect_mysql import conecta
from LotoFacilMySQL.gerarJogos import gerarNumerosJogos, validaResultadosJogoGerado


def fechamento():
    #contadores
    contTrabalhadas = 0
    tentativas = 0
    #vetores
    vetTrabalhadas = list()
    vetJogos = list()
    vetFixas = list()
    # --
    vetorPrimos  = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    vetorMoldura = [1, 2, 3, 4, 5, 6, 10, 11, 15, 16, 20, 21, 22, 23, 24, 25]
    vetImpar     = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
    vetFibo      = [1, 2, 3, 5, 8, 13, 21]
    vetMultiplos = [3, 6, 9, 12, 15, 18, 21, 24]

    # CRIA O VETOR DO ÚLTIMO RESULTADO PARA MONTAR O VETOR REPETIDAS
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor1 = mydb.cursor()
    mycursor1.execute("select max(id_concurso) from jogos")
    last = mycursor1.fetchone()
    last = last[0]
    sql = f"SELECT dezena_1, dezena_2, dezena_3, dezena_4, dezena_5, dezena_6, dezena_7, dezena_8,dezena_9, dezena_10, " \
          f"dezena_11, dezena_12, dezena_13, dezena_14, dezena_15 FROM jogos WHERE id_concurso = {last}"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print("Dezenas sorteadas no concurso anterior: ",end=' ')
    print(result[0])
    ##### fim vetor repetidas

    #seleciona quantidade de jogos
    qdtJogos = int(input("Quantos jogos: "))
    contJogos = 0

    #seleciona quantas dezenas serão trabalhadas nos jogos
    qtd_trabalhadas = int(input("Quantas dezenas trabalhadas: "))

    if qtd_trabalhadas == 25:
        for i in range(1,26):
            vetTrabalhadas.append(i)
    else:
        #captação das dezenas que irá ser usada para gerar os jogos
        while True:
            n = int(input(f"Digite a {contTrabalhadas + 1}° Dezena Trabalhada: "))
            # caso o número digitado não esteja já no vetor, ela é adicionada, e o contador aumenta 1
            if n not in vetTrabalhadas:
                vetTrabalhadas.append(n)
                contTrabalhadas += 1
            # caso dezena já exista no vetor ela não é adicionada e volta ao passo anterior de solicitar uma dezena
            else:
                print("Dezena já incluída")
                continue
            # caso o contador chegar a quantidade de trabalhadas escolhidas, sai do loop while
            if contTrabalhadas == qtd_trabalhadas:
                break

    # solicita se deseja fixar dezenas
    op = int(input("Deseja Fixar dezenas?\n1 - SIM\n2 - NAO\n-->"))
    # se opcao for sim
    if op == 1:
        # solicita a quantidade de dezenas deseja fixar nos jogos
        fx = int(input("Quantas fixas: "))

        # solicita quais as dezenas fixas
        for i in range(0,fx):
            n = int(input(f"{i+1}° fixa: "))
            # se a dezena escolhida for nova é adicionada no vetor
            if n not in vetFixas:
               vetFixas.append(n)

    # fx recebe o tamanho do vetor de fixas
    fx = len(vetFixas)

    # define os parametros da validação
    minImpar = int(input("Minimo Impar: "))
    maxImpar = int(input("Maximo Impar: "))
    minRep   = int(input("Minimo Repetidas: "))
    maxRep   = int(input("Maximo Repetidas: "))
    minPrimo = int(input("Minimo Primo: "))
    maxPrimo = int(input("Maximo Primo: "))
    minMult  = int(input("Mínimo Multiplos: "))
    maxMult  = int(input("Máximo Multiplos: "))
    minFibo  = int(input("Mínimo Fibo: "))
    maxFibo  = int(input("Máximo Fibo: "))
    minMold  = int(input("Mínimo na Moldura: "))
    maxMold  = int(input("Máximo na Moldura: "))
    minSoma  = int(input("Mínimo soma: "))
    maxSoma  = int(input("Máximo soma: "))

    # looping para gerar jogos e os validar
    while True:
        jogo = gerarNumerosJogos()
        # caso a validação seja falsa
        if not valida(jogo, vetTrabalhadas, vetFixas, result, fx,minImpar,maxImpar,minRep,maxRep,
                      minPrimo,maxPrimo,minMult,maxMult,minFibo,maxFibo,minMold,maxMold,minSoma, maxSoma):
            tentativas += 1
            continue
        # caso a validação seja verdadeira
        else:
            if len(vetJogos) > 0:
                # valida se existem jogos ok na validação porém já adicionados no vetor
                if jogo in vetJogos:
                    print(f"Jogo {jogo} repetido")
                    continue
                # caso o jogo não seja repetido é adicionado ao vetor final
                else:
                    vetJogos.append(jogo)
                    # print(f"jogo: {jogo}")
                    # print(f"Gerado com {tentativas} tentativas")
                    # validaResultadosJogoGerado(jogo)
                    tentativas = 0
                    contJogos += 1
            # caso o vetor final não possua jogos ainda o primeiro jogo com validação verdadeira é incluído
            else:
                vetJogos.append(jogo)
                # print(f"jogo: {jogo}")
                # print(f"Gerado com {tentativas} tentativas")
                # validaResultadosJogoGerado(jogo)
                tentativas = 0
                contJogos += 1
                continue
            # caso atinga a quantidade de jogos desejada sai do looping while
            if contJogos == qdtJogos:
                break
            # caso ainda não tenha atingido o número de jogos desejados, continua while
            else:
               continue

    # Abre arquivo onde serão gravados os jogos com permissão de escrita
    file = open("desdobramentos.txt", "w+")

    for index, jogo in enumerate(vetJogos):
        # CONTADORES
        contPrimo = contMold = contRepetidas = contImpar = contTrab = contFixa = contFibo = soma = contMult = 0
        for j in jogo:
            if j in vetorPrimos:
                contPrimo += 1
            if j in vetFibo:
                contFibo += 1
            if j in vetorMoldura:
                contMold += 1
            if j in result[0]:
                contRepetidas += 1
            if j in vetImpar:
                contImpar += 1
            if j in vetTrabalhadas:
                contTrab += 1
            if j in vetFixas:
                contFixa += 1
            if j in vetMultiplos:
                contMult += 1
            soma += j
        # if minImpar <= contImpar <= maxImpar and minPrimo <= contPrimo <= maxPrimo \
        #         and minRep <= contRepetidas <= maxRep and contTrab == 15 and contFixa == fx and minSoma <= soma <= maxSoma \
        #         and minMold <= contMold <= maxMold and minFibo <= contFibo <= maxFibo and minMult <= contMult <= maxMult:
            # imprime no console os jogos com a quantidade de cada parametro
        print(f"\033[1;32m jogo {index+1}:\n      {jogo}\033[1;0m")
        a = validaResultadosJogoGerado(jogo)
        print(a)
        print(f"Qtd de Impar: {contImpar}")
        print(f"Qtd de Primo: {contPrimo}")
        print(f"Qtd de Multiplos de 3: {contMult}")
        print(f"Qtd de Repetida: {contRepetidas}")
        print(f"Qtd de Moldura: {contMold}")
        print(f"Qtd de Fibo: {contFibo}")
        print(f"Soma: {soma}\n")
        print("- -- - -- -" * 10)
        # escreve no arquivo
        file.write(f"jogo {index+1}:\n      {jogo}\n")
        file.write(a)
        file.write("\n")
        file.write(f"Qtd de Impar: {contImpar}\n")
        file.write(f"Qtd de Primo: {contPrimo}\n")
        file.write(f"Qtd de Repetidas: {contRepetidas}\n")
        file.write(f"Qtd de Moldura: {contMold}\n")
        file.write(f"Qtd de Fibo: {contFibo}\n")
        file.write(f"Qtd de Multiplos: {contMult}\n")
        file.write(f"Soma: {soma}\n\n")
        file.write("- -- - -- -" * 10)
        file.write("\n")
    # salva o arquivo com os jogos
    file.close()
    print("\n\n#####  Jogos salvos no arquivo desdobramentos.txt  ######\n\n")

def valida(jogo, vetTrabalhadas, vetFixas, result, fx,minImpar,maxImpar,minRep,maxRep,
                      minPrimo,maxPrimo,minMult,maxMult,minFibo,maxFibo,minMold,maxMold,minSoma,maxSoma):
    # VETORES
    vetorPrimos  = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    vetImpar     = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
    vetorMoldura = [1, 2, 3, 4, 5, 6, 10, 11, 15, 16, 20, 21, 22, 23, 24, 25]
    vetFibo      = [2, 3, 5, 8, 13, 21]
    vetMultiplos = [3,6,9,12,15,18,21,24]
    # CONTADORES
    contPrimo = contRepetidas = contImpar = contTrab = contFixa = soma = contMold = contFibo = contMult = 0
    for j in jogo:
        if j in vetorPrimos:
            contPrimo += 1
        if j in vetMultiplos:
            contMult += 1
        if j in vetFibo:
            contFibo += 1
        if j in result[0]:
            contRepetidas += 1
        if j in vetImpar:
            contImpar += 1
        if j in vetorMoldura:
            contMold += 1
        if j in vetTrabalhadas:
            contTrab += 1
        if j in vetFixas:
            contFixa += 1
        soma += j
    if minImpar <= contImpar <= maxImpar and minPrimo <= contPrimo <= maxPrimo \
            and minRep <= contRepetidas <= maxRep and contTrab == 15 and contFixa == fx and minSoma <= soma <= maxSoma\
            and minMold <= contMold <= maxMold and minFibo <= contFibo <=maxFibo and minMult <= contMult <= maxMult:
        print(f"\n{jogo} OK!\n")
        return True
    else:
        return False
#fechamento()