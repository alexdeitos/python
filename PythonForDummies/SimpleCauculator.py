while True:
    print("Options")
    print("1. somar")
    print("2. diminuir")
    print("3. multiplicar")
    print("4. dividir")
    print("5. sair")

    user_input = int(input("Digite sua opcao: "))

    if user_input==5:
        print("Cauculadora incerrada!")
        break;
    elif user_input == 1:
        num1 = int(input("Digite um numero:"))
        num2 = int(input("Digite outro numero"))
        result = num1 + num2
        print(result)
        continue
    elif user_input == 2:
        num1 = int(input("Digite um numero:"))
        num2 = int(input("Digite outro numero"))
        result = num1 - num2
        print(result)
        continue
    elif user_input == 3:
        num1 = int(input("Digite um numero:"))
        num2 = int(input("Digite outro numero"))
        result = num1 * num2
        print(result)
        continue
    elif user_input == 4:
        num1 = int(input("Digite um numero:"))
        num2 = int(input("Digite outro numero"))
        result = num1 / num2
        print(result)
        continue
    else:
        print("Opção inválida!")
        break