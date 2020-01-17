from time import sleep


def contador(a,b,c):
    print(f'Contagem de {a} até {b} de {c} em {c}:')
    cont = a
    if a < b:
        while cont <=b:
            print(f'{cont} ',end='')
            sleep(0.3)
            cont += c
        print('FIM!')
    else:
        cont = a
        while cont >= b:
            print(f'{cont} ',end='')
            sleep(0.3)
            cont -=c
        print('FIM!')



contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez!!')
a = int(input('INÍCIO: '))
b = int(input('FIM: '))
c = int(input('ITERVALO: '))
contador(a,b,c)
print('<<<< FINALIZADO >>>>')







