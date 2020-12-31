from urllib.request import Request

#link = input("digite o link da web : " + ",headers={'User-Agent': 'Mozilla/5.0'})")
mylink = "https://asloterias.com.br/download-todos-resultados-lotofacil"
myReq = Request(mylink,headers={'User-Agent':'Mozilla/5.0'})




