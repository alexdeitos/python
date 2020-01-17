"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

"""
from datetime import date
ano = int(input("Informe o ano do seu nascimento: "))
idade = date.today().year - ano
if idade > 18:
    print("Venha se alistar! Já passou {} anos do prazo!".format(idade - 18))
elif idade == 18:
    print("Se aliste esse ano!")
else:
    print("Ainda faltam {} anos para você se alistar! Se Acalme!".format(18 - idade))