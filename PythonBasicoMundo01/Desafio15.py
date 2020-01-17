dia = int(input("Digite a quantidade de dias que ficou com o carro: "))
km = float(input("Digite a quantidade de Km's rodados com o carro: "))

preco = (km * 0.15) + (dia * 60)

print("Preço total do aluguel do carro ficou e, R${:.2f}.".format(preco))
