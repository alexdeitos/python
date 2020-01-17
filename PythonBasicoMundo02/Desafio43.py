'''

Leia peso e altura
mostre o IMC de acordo com a tabela
IMC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida

'''

peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura?"))
imc = peso / (altura * altura)
if imc < 18.5:
    print("IMC: {:.1f}\nAbaixo do peso".format(imc))
elif imc >= 18.5 and imc < 25:
    print("IMC: {:.1f}\nPeso Ideal".format(imc))
elif imc >=25 and imc < 30:
    print("IMC: {:.1f}\nAcima do peso".format(imc))
elif imc >=30 and imc < 40:
    print("IMC: {:.1f}\nObesidade".format(imc))
else:
    print("IMC: {:.1f}\nObesidade Mórbida".format(imc))




