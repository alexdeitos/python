from time import sleep
cores = ('\033[m',          # 0 - sem cores
         '\033[0;30;41m',   # 1 - vermelho
         '\033[0;30;42m',   # 2 - verde
         '\033[0;30;43m',   # 3 - amarelo
         '\033[0;30;44m',   # 4 - azul
         '\033[0;30;45m',   # 5 - roxo
         '\033[7;30m',      # 6 - branco
        )


def ajuda(comando):
    título(f'Acessando o manual do comando "{comando}"',4)
    sleep(2)
    print(cores[6], end='')
    help(comando)
    print(cores[0], end='')



def título(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor],end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end='')



# Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP',2)
    sleep(1)
    comando = str(input('Função ou Biblioteca->'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

título('ATÉ LOGO!',1)