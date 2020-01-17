frase = input("Digite:").strip().upper()
print(frase)
palavras = frase.split()
print(palavras)
junto = ''.join(palavras)
inverso=junto[::-1]
print("o inverso de {} é {}".format(junto,inverso))
if junto == inverso:
    print("É palindromo!")
else:
    print("Não é palindromo!")