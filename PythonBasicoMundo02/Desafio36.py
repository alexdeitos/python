'''

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado

'''

valor_casa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite seu salário: R$"))
tempo = int(input("Em quantos anos deseja pagar? "))
parcela = valor_casa  / (tempo * 12)
if parcela > (salario * 30) / 100:
    print("Empréstimo negado! Parcela de R${:.2f} excede 30% do salário!".format(parcela))
else:
    print("Empréstimo concedido pagamento será de {} vezes de R${:.2f}".format(tempo*12,parcela))
