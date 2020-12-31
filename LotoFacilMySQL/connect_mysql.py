from mysql import connector as con


def conecta():
    conexao = con.connect(
          host="localhost",
          user="seq_user",
          passwd="seq_password",
          database="projetoweb"
    )
    return conexao