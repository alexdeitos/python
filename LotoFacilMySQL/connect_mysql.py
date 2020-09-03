import mysql.connector

def conecta():
    conexao = mysql.connector.connect(
          host="localhost",
          user="seq_user",
          passwd="seq_password",
          database="projetoweb"
    )
    return conexao