'''

Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

'''
salario = float(input("Digite seu salário: R$"))
if salario > 1250 :
    aumento = salario + ((10 * salario) / 100)
    x = 10
else:
    aumento = salario + ((15 * salario) / 100)
    x = 15
print("Seu salário de R${:.2f} recebeu um aumento de {}% e passa a valer R${:.2f}".format(salario,x,aumento))