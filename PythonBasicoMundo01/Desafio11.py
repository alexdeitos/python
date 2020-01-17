a = float(input("digite a altura: "))
l = float(input("Digite a largura"))

total = a * l

totalTinta = total / 2

print("Sua parede tem {:.1f} x {:.2f}m e sua área é de {:.3f}m².".format(l,a,total))
print("Para pintar essa parade você precisará de {:.4f}L de tinta.".format(totalTinta))
