num = int(input("Digite o número:\n=>"))
primo = 0
for c in range(1,num+1):
    if num % c == 0 :
        print('\033[33m',end = ' ')
        primo += 1
    else:
        print('\033[31m',end = ' ')
    print("{}".format(c),end='')

if primo > 2:
   print("\n\033[mO número {} foi divisível {} vezes, então não é primo!".format(num,primo))
else:
    print("\n\033[mO número {} foi divisível {} vezes, então é primo!".format(num, primo))
print("""
legenda:
amarelo = divisível
vermelho = não divisível
""")
