"""

Crie um sistema que gere um número entre 0 e 5
leia uma aposta do usuário
mostre se ele acertou ou não

"""
from random import randint
from time import sleep

n = randint(0,5)
print("--=--" * 20)
print("Pensei em um número entre 0 a 5, você consegue adivinhar qual é?")
print("--=--" * 20)
a = int(input("Digite seu palpite:"))
print("PROCESSANDO....")
sleep(2)
if a == n :
   print("Você acertou, o número que pensei também era o {}".format(n))
else:
   print("Você perdeu! Eu pensei no número {} e não no {}".format(n,a))


