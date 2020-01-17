"""

mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

"""
num = int(input("Digite o número para ver a tabuada do mesmo: "))
for c in range(1,11):
    print("{} X {} = {}".format(c,num,c*num))
