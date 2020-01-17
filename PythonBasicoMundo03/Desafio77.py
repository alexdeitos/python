palavras = ('AVIÃO', 'CARRO' , 'FUTEBOL', 'SKATE','PYTHON','JAVA','CHUVA','ARVORE','NATUREZA')
count = 0
for x in range(0,len(palavras)):
    print(f"\nNa palavra {palavras[x]} temos as vogais:", end=' ')
    for i in palavras[x]:
        if i in 'AEIOUÃ':
            print(i,end=' ' )
print('\n')
