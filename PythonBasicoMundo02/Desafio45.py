from random import randint
from time import sleep

pc = randint(0,2)
ganhador = "invalido"

while ganhador == "invalido":
    print("VAMOS JOGAR PAPEL PEDRA OU TESOURA!")
    print("""Suas opções:
    [ 0 ] PAPEL
    [ 1 ] PEDRA
    [ 2 ] TESOURA
    """)
    try:
        usuario = int(input("Digite sua escolha:\n==>"))
    except ValueError:
        print("\nOPÇÃO INVÁLIDA!!! ESCOLHA ENTRE 0 , 1 e 2\n")
        continue
    if usuario == 0 and pc == 1:
        ganhador = "Você ganhou com PAPEL sobre PEDRA!"
    elif usuario == 1 and pc == 0:
        ganhador = "PC ganhou com PAPEL sobre PEDRA!"
    elif usuario == 0 and pc == 2:
        ganhador = "PC ganhou com TESOURA sobre PAPEL!"
    elif usuario == 2 and pc == 0:
        ganhador = "Você ganhou com TESOURA sobre PAPEL!"
    elif usuario == 1 and pc == 2:
        ganhador = "Você ganhou com PEDRA sobre TESOURA!"
    elif usuario == 2 and pc == 1:
        ganhador = "PC ganhou com PEDRA sobre TESOURA!"
    elif usuario == pc :
        ganhador = "EMPATOU!"
    else:
        print("\nOPÇÃO INVÁLIDA!!! ESCOLHA ENTRE 0 , 1 e 2\n")
    continue

print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO")
sleep(0.5)
print("# "*30 + ganhador + " #"*30)




