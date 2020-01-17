'''

Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário,
2 para octal e
3 para hexadecimal.

'''

num = int(input("Digite um número inteiro: "))
print("[ 1 ] Binária")
print("[ 2 ] Octal")
print("[ 3 ] Hexadecimal")
base = int(input("Escolha uma base para conversão: "))
if base == 1:
    print("{} convertido para binário fica {}".format(num,bin(num)[2:])) # o [2:] vai pegar o resultado do index 2 até o final da string
elif base == 2:
    print("{} convertido para binário fica {}".format(num, oct(num)[2:]))
elif base == 3:
    print("{} convertido para binário fica {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida! Tente novamente!")




