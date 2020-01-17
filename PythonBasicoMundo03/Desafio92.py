from datetime import datetime
pessoa={}
pessoa['nome'] = str(input('Nome: '))
pessoa['nascimento'] = int(input('Ano de Nascimento: '))
pessoa['idade'] = datetime.now().year - pessoa['nascimento']
ct = int(input('Carteira de trabalho (0 não tem): '))
if ct == 0:
    pessoa['carTrabalho'] = 'não informada!'
if ct != 0:
    pessoa['carTrabalho'] = ct
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratacao'] + 35) - datetime.now().year)
print('-=' * 30)
print(f"Nome: {pessoa['nome']}\n"
      f"Data de Nascimento: {pessoa['nascimento']}\n"
      f"Idade: {pessoa['idade']}\n"
      f"Carteira de trabalho: {pessoa['carTrabalho']}\n"
      f"Ano da contratação: {pessoa['contratacao']}\n"
      f"Salário: {pessoa['salario']}\n"
      f"Se aposenta com : {pessoa['aposentadoria']} anos")
