""" leia nomes de alunos e sorteie um para ajudar o professor nas atividades """

# choice é o método para fazer uma escolha dentro da lista
from random import choice

x = 0
alunos = []
qtde_alunos = int(input("Quantos alunos deseja inserir: "))

while x < qtde_alunos:
    alunos.insert(x,(input("Digite o nome do Aluno:")))
    x += 1

sorteio = choice(alunos)
print("O aluno sorteado para auxiliar nas atividades foi:\n {}".format(sorteio))



