print("---"*20)
print(" "*19+" Sequencia Fibonacci")
print("---"*20)

#programa funcional incia aqui

n = int(input("Quantos termos você quer mostrar:\n==>")) #Quantidade de números você quer impressos na Tela
t1 = 0            # cria a primeira variável
t2 = 1            # cria a segunda variável
print("{} -> {}".format(t1,t2),end='')
cont = 3          # contador inicia em 3 pois os dois primeiros já foram impresssos acima
while cont <= n:
    t3 = t1 + t2  # o resultado é a soma dos dois anteriores
    print(" -> {}".format(t3),end='')
    t1 = t2       # move a primeira variavel 1 casa para frente
    t2 = t3       # move a 2 variável 1 casa para frente
    cont +=1      # adiciona 1 unidade ao contador
print(" -> Fim")  # sai do laço de repetição e finaliza o programa