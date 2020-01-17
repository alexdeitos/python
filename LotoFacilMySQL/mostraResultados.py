from LotoFacilMySQL.connect_mysql import conecta


def mostraResultados():
    mydb = conecta()
    mycursor = mydb.cursor()

    sql = "select * from jogos"
    mycursor.execute(sql)
    resultado = mycursor.fetchall()

    for jogo in resultado:
        print(f"Concurso {jogo[0]:^4} Dezenas: {jogo[1]:^4} - {jogo[2]:^4} - {jogo[3]:^4} - {jogo[4]:^4} - {jogo[5]:^4}"
              f" - {jogo[6]:^4} - {jogo[7]:^4} - {jogo[8]:^4} - {jogo[9]:^4} - {jogo[11]:^4} - {jogo[12]:^4} - "
              f"{jogo[13]:^4} - {jogo[14]:^4} - {jogo[15]:^4}")

