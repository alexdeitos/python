num = tuple(int(input(f'Digite o {i+1}º numero: ')) for i in range(4))
print(f"O número 9 foi digitado {num.count(9)} vezes!")
if 3 in num:
    print(f"O número 3 foi digitado na {num.index(3)+1}º posição!")
else:
    print("O valor 3 não foi digitado!")
print("Os números digitados que são pares são: ",end='')
for pair in num:
    if pair % 2 == 0:
        print(pair,end=' ')
