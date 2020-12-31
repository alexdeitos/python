from LotoFacil.PatternFill_testes import formata_resultados
from LotoFacil.confere_jogo import validadorResultados
from LotoFacil.geraJogo import gerarNumerosJogos
from LotoFacil.geraJogo import validandoParametros


def __main__():
    cont = 0
    cont1 = 0
    f = open('jogos.txt', 'w+')

    while True:
        opcao = int(input('O que deseja ?\n[1] - Gerar Jogos\n[2] - Formatar resutlados\n[3] - Validar Jogos\n'
                          '[4] - Finalizar programa\n=> '))
        if opcao == 1:
            qtdJogos = int(input('Quantos Jogos? '))
            while True:
                    v = gerarNumerosJogos()
                    if validandoParametros(v):
                        cont1 += 1
                        print('=-=-=-=' * 5)
                        print(f'\033[1;32m Jogo que atende os parametros: {v} \033[1;0m')
                        f.write(f'{v}\n')
                        print(f'Foram necessarios {cont} jogos!')
                        print('=-=-=-=' * 5)
                        print()
                    cont += 1
                    if qtdJogos == cont1:
                        f.close()
                        break
        elif opcao == 2:
            formata_resultados()
            continue
        elif opcao == 3:
            validadorResultados()
            continue
        elif opcao == 4:
            print('\033[33m Finalizado com sucesso! Até mais!\033[0m')
            break
        else:
            print(f'\033[31m Opcao {opcao} é inválida! \033[0m')


if __name__ == '__main__':
    __main__()