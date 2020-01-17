
palavra_secreta = "python"
aposta = ""
contador_aposta = 0
limite_apostas  = 3
sem_apostas = False

while aposta != palavra_secreta and not(sem_apostas):
    if contador_aposta < limite_apostas:
        aposta = input("Digite sua aposta: ")
        contador_aposta +=1
    else:
        sem_apostas = True

if sem_apostas:
    print("Game Over! Você não descobriu a palavra secreta!!!")
else:
    print("Parabéns! Você digitou {} e acertou a palavra secreta!!!".format(palavra_secreta))







