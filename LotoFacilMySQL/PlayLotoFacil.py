from LotoFacilMySQL.add_new_sorteio_banco import adicionaResultado
from LotoFacilMySQL.add_todos_sorteios_banco import addTodosSorteios
from LotoFacilMySQL.connect_mysql import conecta
from LotoFacilMySQL.formata_arquivo import formata
from LotoFacilMySQL.geraDesdobramentos import fechamento
from LotoFacilMySQL.gerarJogos import gerarNumerosJogos, validandoParametros, validaResultadosJogoGerado
from LotoFacilMySQL.limpa_banco import excluiJogos
from LotoFacilMySQL.mostraResultados import mostraResultados
from LotoFacilMySQL.validaResultados import validadorResultados


def __main__():
    print('#####' * 20)
    print(f"{'Seja bem vindo ao PlayLotoFácil! - Criado por Alexsandro Deitos':^100}")
    print(f"{'Escolha a sua opção e boa sorte!':^100}")
    print('#####' * 20)
    global result

    # CRIA O VETOR DO ÚLTIMO RESULTADO PARA MONTAR O VETOR REPETIDAS
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor1 = mydb.cursor()
    mycursor2 = mydb.cursor()
    mycursor2.execute("select count(*) from jogos")
    countjogos = mycursor2.fetchone()
    if countjogos[0] ==  0 :
        print("\n\nTabela de jogos vazia, importe novamente os resultados!\n")
    else:
        mycursor1.execute("select count(*) from jogos")
        last = mycursor1.fetchone()
        last = last[0]
        sql = f"SELECT dezena_1, dezena_2, dezena_3, dezena_4, dezena_5, dezena_6, dezena_7, dezena_8,dezena_9, dezena_10, " \
              f"dezena_11, dezena_12, dezena_13, dezena_14, dezena_15 FROM jogos WHERE id_concurso = {last}"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print("\n\nÚltimo resultado contido no banco de dados:\n")
        print(f"Concurso: {last}\nDezenas: ", end=' ')
        for j in result[0]:
            print(j, end='\n' if j == result[0][-1] else " - ")
        ##### fim vetor repetidas

    while True:
        print('\n\nO que deseja:\n')
        opcao = str(input('[ 1 ] - Gerar Jogos\n[ 2 ] - Formatar Resultados\n[ 3 ] - Conferir Resultados\n'
                          '[ 4 ] - Operações Avançadas - Banco de Dados\n[ 5 ] - Gerar Fechamento\n'
                          '[ 6 ] - Visualiza resultados\n'
                          '[ 7 ] - Sair\n\n==>> '))
        if opcao == '1':
            cont = 0
            cont1 = 0
            print()
            print('=-=-=-=' * 5)
            qtdJogos = int(input('\n\nDeseja gerar quantos jogos?\n\n==> '))
            f = open('jogos.txt', 'w+')
            # define os parametros da validação
            minImpar = int(input("Minimo Impar: "))
            maxImpar = int(input("Maximo Impar: "))
            minRep   = int(input("Minimo Repetidas: "))
            maxRep   = int(input("Maximo Repetidas: "))
            minPrimo = int(input("Minimo Primo: "))
            maxPrimo = int(input("Maximo Primo: "))
            minFibo  = int(input("Minimo Fibo: "))
            maxFibo  = int(input("Maximo Fibo: "))
            minMult  = int(input("Minimo Multiplos de 3: "))
            maxMult  = int(input("Maximo Multiplos de 3: "))
            minMold  = int(input("Minimo na Moldura: "))
            maxMold  = int(input("Maximo na Moldura: "))
            while True:
                v = gerarNumerosJogos()
                if validandoParametros(v,result,minImpar,maxImpar,minRep,maxRep,minPrimo,maxPrimo,minMold,maxMold,
                                       minFibo,maxFibo,minMult,maxMult):
                    cont1 += 1
                    print('=-=-=-=' * 5)
                    print(f'\033[1;32m Jogo que atende os parametros: {v} \033[1;0m')
                    f.write(f'{v}\n')
                    print(f'Foram necessarios {cont} jogos!')
                    a = validaResultadosJogoGerado(v)
                    print(a)
                    print('=-=-=-=' * 5)
                    print()
                cont += 1
                if qtdJogos == cont1:
                    f.close()
                    break
        elif opcao == '2':
            print()
            formata()
            continue
        elif opcao == '3':
            print()
            validadorResultados()
            continue
        elif opcao == '4':
            print('=-=-=-=' * 5)
            print('Atenção isso pode afetar as informações no banco de dados! Tenha cautela! O que deseja fazer?')
            print('=-=-=-=' * 5)
            while True:
                op = str(input('\n[ 1 ] - Atualiza Lista de Resultados\n'
                               '[ 2 ] - Importa todos os resultados para o banco de dados (Certifique-se de que '
                               'o arquivo loto.xlsx está na pasta raiz!)\n'
                               '[ 3 ] - Exclui todos os jogos do banco de dados\n'
                               '[ 4 ] - Menu Principal\n\n==>> '))
                if op == '1':
                    adicionaResultado()
                elif op == '2':
                    addTodosSorteios()
                elif op == '3':
                    excluiJogos()
                elif op == '4':
                    print('=-=-=-=' * 5)
                    print('Voltando ao menu...')
                    break
                else:
                    print('=-=-=-=' * 5)
                    print('Opção inválida!')
                    print('=-=-=-=' * 5)
                    continue
        elif opcao == '5':
            fechamento()
            continue
        elif opcao == '6':
            mostraResultados()
            continue
        elif opcao == '7':
            print('=-=-=-=' * 5)
            print('\033[33m Finalizado com sucesso! Até mais!\033[0m')
            print('=-=-=-=' * 5)
            exit()
        else:
            print('=-=-=-=' * 5)
            print('Opção inválida!')
            print('=-=-=-=' * 5)
            continue

if __name__ == '__main__':
    __main__()