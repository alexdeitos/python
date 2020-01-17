"""

Média de 2 notas

"""

nota01 = float(input("Primeira nota:"))
nota02 = float(input("Segunda nota:"))

media = (nota01 + nota02) / 2
if media < 5.0 :
    situacao = "REPROVADO"
elif media >= 5.0 and media <= 6.9:
    situacao ="em RECUPERAÇÃO"
else:
    situacao = "APROVADO"

print("A media do aluno foi de {:.1f} e ele está {}".format(media,situacao))