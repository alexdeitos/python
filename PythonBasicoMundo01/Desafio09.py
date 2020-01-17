# Leia um número e imprima sua tabuada


num = int(input("Numero: "))
print("=" * 12)
for i in range(11):
    result = num * i
    print("{} * {:2} = {}".format(num, i , result))
    i += i
print("=" * 12)