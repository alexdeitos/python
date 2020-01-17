print("GERADOR DE PROGRESSÃO ARITIMÉTICA")
print("=-="*10)
termo = int(input("Primeiro termo:\n==>"))
razao = int(input("Razão da PA:\n==>"))
termos = int(input("Quantos termos deseja mostrar:\n==>"))
c = 1
cont = 0
while c <= termos:
    print("{}".format(termo), end=' -> ')
    termo +=razao
    c +=1
    cont +=1
print(" PAUSA")
i = 1
while i != 0:
    l = int(input("\nQuantos termos você quer mostrar a mais? Digite 0 caso queira finalizar:\n==>"))
    if l == 0 :
        i = 0
        continue
    c = 1
    while c <= l:
        print("{}".format(termo), end=' -> ')
        termo += razao
        cont +=1
        c +=1
    print("PAUSA")
print("=-="*10)
print("\nAcabou! Com {} termos mostrados".format(cont))
