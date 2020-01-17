"""

A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER

"""
from datetime import date
nascimento = int(input("Digite o ano em que você nasceu: "))
idade = date.today().year - nascimento
if idade <=9 :
    categoria = "MIRIM"
elif idade > 9 and idade <= 14:
    categoria = "INFANTIL"
elif idade > 14 and idade <= 19:
    categoria = "JUNIOR"
elif idade > 19 and idade <= 25:
    categoria = "SENIOR"
elif idade > 25 :
    categoria = "MASTER"
else:
    print("Você digitou uma idade inválida!")
print("FICHA DO ATLETA:\nIDADE: {}\nCATEGORIA: {}".format(idade,categoria))


