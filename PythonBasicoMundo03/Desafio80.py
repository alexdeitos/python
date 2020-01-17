num = []
for x in range(0,5):
    v = int(input("Digite um valor: "))
    if x == 0 or v > num[-1]:
        num.append(v)
        print("Adicionado ao final da lista...")
    else:
        pos = 0
        while pos < len(num):
            if v <= num[pos]:
                num.insert(pos,v)
                print(f"Adicionado a posição {pos} da lista...")
                break
            pos +=1
print(f'lista {num}')
