from LotoFacilMySQL.connect_mysql import conecta


def excluiJogos():
    i = 0
    mydb = conecta()
    while True:
        if i == 1:
            break
        op = str(input("Tem certeza que deseja excluir os dados da tabela jogos?\n[ 1 ] - SIM\n[ 2 ] - NAO\n==>>  "))
        if op == '1':
            mycursor = mydb.cursor()
            opcao = str(input('[ 1 ] - Deletar todos\n[ 2 ] - Deletar concurso específico\n\n=>> '))
            while True:
                if opcao == '1':
                    sql = "delete from jogos;"
                    sql2 = "alter table jogos auto_increment=1;"
                    mycursor.execute(sql)
                    mycursor.execute(sql2)
                    print('Registros deletados com sucesso!')
                    i = 1
                    break
                elif opcao == '2':
                    id = str(input('Digite a ID do concurso:\n=>> '))
                    sql = f'delete from jogos where id_concurso={id};'
                    sql2 = f'ALTER TABLE jogos AUTO_INCREMENT={id};'
                    mycursor.execute(sql)
                    mycursor.execute(sql2)
                    print(f'Concurso {id} deletado com sucesso')
                    break
                else:
                    print('Opção inválida!')
                    continue
        elif op == '2':
            print('OK!')
            break
        else:
            print('Opção inválida!')
            continue
    mydb.commit()
    mydb.close()

