"""
Leia uma frase e
quantas letras "a" tem
em que posição a letra "a" aparece pela primeira vez
em que posição a letra "a" aparece a última vez

"""
frase = str(input("Digite uma frase: ")).lower().strip()
print("Quantidade: {}".format(frase.count("a")))
print("A Letra aparece primeiro na casa: {}".format(frase.find("a")+1))
print("A Letra aparece por último na casa: {}".format(frase.rfind("a")+1))
