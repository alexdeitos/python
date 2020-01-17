n1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
soma = n1
a = 10
while a > 0:
    print(soma, end='')
    print(' -> ' if a > 1 else '', end='')
    soma += r
    a -= 1
    if a == 0:
        a = int(input('\nVocê quer mostrar mais quantos termos? '))
