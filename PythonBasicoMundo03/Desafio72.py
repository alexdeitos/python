'''

Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

'''

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove'
           ,'vinte')
while True:
    i = int(input("Qual número deseja de 0 a 20: "))
    if (i < 0) or (i > 20):
        print("Número inválido! Tente novamente")
        continue
    print(f'Você digitou o número {extenso[i]}')
    op = str(input("\nDeseja continuar [S/N]")).strip().upper()[0]
    while op not in 'SN':
        op = str(input("Opção Inválida! Deseja continuar [S/N]")).strip().upper()[0]
    if op == 'N':
        break
print("Programa finalizado com sucesso!")








