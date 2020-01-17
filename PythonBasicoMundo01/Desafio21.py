""" Crie um programa que leia um arquivo mp3 e toque o mesmo """

import playsound


op = int(input("1. Tocar\n2. Sair\nOpção: "))
if op == 1:
    playsound.playsound("bob.mp3")
else:
    quit()

