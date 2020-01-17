#posicoes:

frase = "     Curso em Video Python   "
x=0
print(frase)
frase = frase.strip() # remove os espaços do início e do final
"""for letter in frase:
    print(x,letter)
    x+=1
"""
print(frase)
print(frase[2::2])
print(frase[::2])
frase = frase.replace("Curso","apostila")
print(frase)

print(len(frase)) # tamanho da string

print("apostila" in frase) # procura a palavra em frase

print(frase.upper().count("A"))
print(frase.count("a"))

# frase[posicao inicial:posicao final:intervaloPulos]
# se deixa vazio no inicio ele comeca de zero
# se deixa vazio o final ele considera a string até o último caracter

frase = frase.replace("Curso","apostila")
dividido = frase.split()
print(dividido)
print(dividido[2])
print(dividido[2][3])
