from time import sleep


def maior (*num):
    cont= m = 0
    print('\nAnalisando os valores passados')
    for n in num:
        print(f'{n}',end=' ')
        sleep(0.2)
        if cont == 0 :
            m = n
        else:
            if n > m :
                m = n
        cont += 1
    print(f' Foram informados {cont} valores ao todo!')
    print(f'\nO maior número de foi {m}!\n')
    print('-=' * 15)


maior(4,3,6,8,9,10,23)
maior(4,3,6,)
maior(4,3,6,10,23)
maior(23)
maior()