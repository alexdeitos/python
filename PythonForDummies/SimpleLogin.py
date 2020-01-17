#Importar as cenas que sao precisas
from tkinter import *
import pymysql
import ttkSimpleDialog
import gui
#Criar a Janela e botao de sair
top = Tk()
top.minsize(width=1115, height=110)
janela = Frame(top)
janela.pack()
botao = Button(janela, text="SAIR", command=janela.quit)
botao.pack()
"""
#Ler login e password
username = input("LOGIN" , "Introduza o UserName:")
password = input("LOGIN", "Introduza a Password:", show="*")
#Ligar a bd remota
db = pymysql.connect(host="127.0.0.1",user="softpharma", passwd="NwSoftPs1843", db="python")
cursor = db.cursor()
cursor.execute("SELECT * FROM login")
result = cursor.fetchall()
#Verificar se dados sao validos
for record in result:
	if username == record[0]:
		if password == record[1]:
			ttkSimpleDialog.showinfo ("LOGIN" , "Login correcto")
			"""
janela.mainloop()
