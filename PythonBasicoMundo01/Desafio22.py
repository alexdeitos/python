"""
Leia um nome completo de uma pessoa e:
mostre tudo maiusculo
mostre tudo minusculo
quantas letras tem, sem considerar os espaços
quantas letras tem o primeiro nome

"""
x=0
nome = str(input("Digite seu nome completo: ")).strip()

for letter in nome:
    if letter.isspace():
        continue
    else:
        x +=1
print("Seu nome completo em letras maiusculas: {}".format(nome.upper()))
print("Seu nome completo em letras minusculas: {}".format(nome.lower()))
print("Seu nome possui {} letras sem contar espaços".format(x))
print("Seu nome possui {} letras sem contar espaços".format(len(nome)-nome.count(" ")))
print("Seu primeiro nome tem {} letras".format(len(nome.split()[0])))


