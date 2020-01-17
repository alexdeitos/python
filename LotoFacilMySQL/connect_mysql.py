import mysql.connector

def conecta():
    conexao = mysql.connector.connect(
          host="192.168.162.28",
          user="seq_user",
          passwd="seq_password",
          database="projetoweb"
    )
    return conexao