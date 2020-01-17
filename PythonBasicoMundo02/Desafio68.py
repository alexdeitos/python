from random import randint
ganhou = 0
print("=-="*10)
print("VAMOS JOGAR PAR OU ÍMPAR!")
print("=-="*10)
while True :
    n = int(input("Digite um Valor:\n=>"))
    pc = randint(0, 10);
    op = ' '
    while op not in 'PI':
        op = input("PAR ou IMPAR? [P/I]\n=>").strip().upper()[0]
    print(f"Voce jogou {n} e o compudador jodou {pc}. Total {n+pc}")
    if op == 'P':
        if (pc+n)%2==0:
            print("voce ganhou!")
            ganhou +=1
            continue
        else:
            print("=-=" * 10)
            print(f"GAME OVER! Computador Ganhou!", end=' ')
            break
    elif op == 'I':
        if (pc+n) % 2 != 0:
            print("Você ganhou!")
            ganhou +=1
            continue
        else:
            print("=-=" * 10)
            print("GAME OVER! Computador Ganhou!",end=' ')
            break
print(f'Você ganhou {ganhou} vezes.')