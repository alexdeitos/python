from LotoFacilMySQL.connect_mysql import conecta

def adicionaResultado():

    j = list()
    cont = 0
    print("\n\nInforme as 15 dezenas do resultado:\n\n")
    while True:
        mydb = conecta()
        mycursor = mydb.cursor()
        for x in range(0,15):
            j.append(int(input(f'Digite a dezena {x+1}: ')))
        n1 = j[0]
        n2 = j[1]
        n3 = j[2]
        n4 = j[3]
        n5 = j[4]
        n6 = j[5]
        n7 = j[6]
        n8 = j[7]
        n9 = j[8]
        n10 = j[9]
        n11 = j[10]
        n12 = j[11]
        n13 = j[12]
        n14 = j[13]
        n15 = j[14]
        sql = f'insert into jogos (dezena_1, dezena_2, dezena_3, dezena_4, dezena_5, dezena_6, dezena_7, dezena_8,' \
              f'dezena_9, dezena_10, dezena_11, dezena_12, dezena_13, dezena_14, dezena_15)' \
              f'values({n1},{n2},{n3},{n4},{n5},{n6},{n7},{n8},{n9},{n10},{n11},{n12},{n13},{n14},{n15})'
        mycursor.execute(sql)
        mydb.commit()
        mydb.close()
        cont += 1
        j.clear()
        print("Resultado inserido com sucesso!\n")
        op = int(input("\nDeseja inserir mais resultados:\n[ 1 ] - SIM\n[ 2 ] - NAO\n==> "))
        if op == 1:
            continue
        elif op == 2:
            print(f"\nBanco de dados atualizado com {cont} resultados!\n")
            break
        else:
            print("\nOpção inválida!\n")