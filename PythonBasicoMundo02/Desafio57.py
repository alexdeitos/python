'''

Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto

'''

i = 0
while i == 0:
    sexo = input("Informe seu sexo [M / F] ").upper()
    if sexo != 'M' and sexo != 'F':
        print("sexo invalido! Escolha M ou F")
        continue
    else:
        print("Sexo {} registrado com sucesso!".format(sexo))
        i = 1