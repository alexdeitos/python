valida = bool
while valida:
    n = int(input("Qual é o número a ser validado: "))
    i = a = r = 0
    b = 1
    fibo = False
    while i <= n:
        if r == n:
            fibo = True
        r = b + a
        a = b
        b = r
        i += 1
    if fibo :
        print(f"Número {n} pertence a sequencia de Fibonacci!")
    else:
        print(f"Número {n} não pertence a sequencia de Fibonacci!")
    v = int(input("\n\nDeseja validar outro número: \n [1] - SIM \n [2] - NAO\n\n==>"))
    if v == 1:
        continue
    elif v == 2:
        print("Valeu!")
        break
    else:
        print("\n\nOpçao inválida! Continuando entao...\n\n")
        continue