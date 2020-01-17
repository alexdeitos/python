aluno = {}
aluno['nome']= str(input('Digite o nome: '))
aluno['media']=float(input(f'Digite a media de {aluno["nome"]}: '))
if aluno['media'] > 6.0:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
print(f"O aluno {aluno['nome']} está {aluno['situacao']}.")

