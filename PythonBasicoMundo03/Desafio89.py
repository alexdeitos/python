lista = []
while True:
    nome = (str(input('Nome: ')))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome,[nota1,nota2],media])
    opcao = str(input("Deseja continuar? [S/N]: ")).strip()[0]
    if opcao in 'Nn':
        break
print('-=' * 30)
print(f"{'No':<4}{'NOME':<10}{'MEDIA':>8}")
print('-'*26)
for i,a in enumerate(lista):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.2f}")
while True:
    print('-=' * 35)
    opc = int(input("Deseja ver as notas de qual aluno: (999 para interromper): "))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(lista)-1:
        print(f"Notas de {lista[opc][0]} são {lista[opc][1]}")
print("<<<< VOLTE SEMPRE >>>>>")

