"""

Leia uma velocidade
se for menos de 80km segue viagem
se for mais de 80 multa
acima de 80km, R$7 de multa por Km

"""

km = float(input("Digite a velocidade do carro: "))
if km <= 80:
    print("Velocidade dentro do permitido! Pode continuar!")
else:
    multa = (km - 80) * 7
    print("Velocidade acima do permitido! Multa de R${:.2f} aplicada!".format(multa))
