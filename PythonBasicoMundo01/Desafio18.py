""" Leia um angulo e mostre seu Seno, consseno e a tangente desse angulo """

from math import sin, cos, tan,radians

"""
def seno(angulo):
    return sin(angulo),cos(angulo),tan(angulo)
"""
angulo = float(input("Digite um angulo: "))
seno = sin(radians(angulo))
co = cos(radians(angulo))
ta = tan(radians(angulo))

print("Para um angulo de {} seu seno é {:.2f}".format(angulo,seno))
print("Para um angulo de {} seu cosseno é {:.2f}".format(angulo,co))
print("Para um angulo de {} seu tangente é {:.2f}".format(angulo,ta))

