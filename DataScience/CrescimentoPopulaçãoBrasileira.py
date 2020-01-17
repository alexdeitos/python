# Crescimento população Brasil entre 1980 e 2016
# DataSus
import matplotlib.pyplot as plt

dados = open("populacao-brasileira.csv").readlines() # abre o arquivo e já le as linhas

x = [] # lista para anos
y = [] # lista para população

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.bar(x,y, color="#c1c1c1")
plt.plot(x,y, color="k", linestyle="--")

plt.title("Crescimento população Brasil entre 1980 e 2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
plt.savefig("populacao_brasileira.png", dpi=300)
plt.show()
