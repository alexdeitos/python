def leiaInt(texto):
    n = input(texto)
    if n.isnumeric():
        return n
    else:
        while True:
            print('\33[31mErro!Digite um número inteiro válido!\33[m')
            n = input(texto)
            if n.isnumeric():
                break
        return n


n = leiaInt('Digite um numero: ')
print(f'Você digitou o número {n}')
