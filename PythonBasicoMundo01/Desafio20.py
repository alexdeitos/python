""" Leia nome de alunos e sorteia a ordem de apresentacao de trabalhos """

# shuffle é o método para embaralhar
from random import shuffle

x = 0
alunos = []
qtde_alunos = int(input("Quantos alunos deseja inserir: "))

while x < qtde_alunos:
    alunos.insert(x,(input("Digite o nome do Aluno:")))
    x += 1

shuffle(alunos)
print("Ordem apresentacao de trabalhos: ")
y=1
for aluno in alunos:
    print("{}°".format(y),aluno)
    y+=1




