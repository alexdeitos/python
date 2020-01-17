import matplotlib.pyplot as plt

# Documentação matplotlib.pyplot
# Fonte: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html


lista = [1,2,3,4,5,5,6,4,5]

x = [1,3,5,7,9]
y = [5,2,3,4,7]

x1 = [2,4,6,8,10]
y1 = [3,4,6,9,2]

# Legendas do Gráfico
titulo = "Gráfico Python"
eixox  = "Eixo x"
eixoy  = "Eixo y"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

# Gráfico de Barras
#plt.bar(x,y ,label='Impares')
#plt.bar(x1,y1,label='Pares')
#legendas
#plt.legend();

# Gráficos de pontos
plt.scatter(x,y, label="Meus Pontos")
# GRafico de linhas (nesse caso vai ligar os pontos)
plt.plot(x,y)
plt.legend();


# Construtor do Gráfico
plt.show();