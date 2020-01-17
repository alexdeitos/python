'''

Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

'''
from random import randint

pc = randint(0,10)
acertou = False
c = 0

print("SOU SEU COMPUTADOR...ACABEI DE PENSAR EM UM NÚMERO ENTRE 0 E 10, CONSEGUE ADVINHAR ?")

while not acertou:
    palpite = int(input("Digite seu palpite\n=>"))
    c += 1
    if palpite == pc:
        acertou = True
    if palpite > 10:
        print("Seu palpite foi inválido! Escolha entre 1 e 10")
        c -= 1
        continue
    if palpite > pc :
        print("menos...Tente mais uma vez!")
    if palpite < pc :
        print("mais...Tente mais uma vez!")

print("Acertou com {} tentativas. Parabéns!".format(c))
