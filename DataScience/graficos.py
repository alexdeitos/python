import matplotlib.pyplot as plt

# Documentação matplotlib.pyplot
# Fonte: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

'''
lista = [1,2,3,4,5,5,6,4,5]

x = [1,3,5,7,9]
y = [5,2,3,4,7]

x1 = [2,4,6,8,10]
y1 = [3,4,6,9,2]
'''
#lista=[17,12,13,22,20,24,25,9,21,18,5,10,16,3,7]
#lista=[16,18,7,15,11,20,9,8,17,10,2,21,5,24,19]
#lista=[10,17,22,8,4,13,24,16,9,2,7,11,20,25,1]
#lista=[3,12,18,4,15,2,16,9,8,10,7,24,22,25,11]
#lista=[23,20,12,24,21,19,16,4,1,9,5,3,14,11,13]
#lista=[25,11,10,22,13,16,6,15,18,2,21,14,24,17,8]
#lista=[21,11,12,23,22,2,8,10,5,4,17,9,14,16,13]
#lista=[7,1,17,19,13,5,9,3,21,16,6,24,4,18,25]
#lista=[5,22,12,16,9,24,20,25,7,2,8,1,18,3,13]
#lista=[6,14,17,24,12,21,13,16,2,15,7,9,4,8,11]

lista = [196, 173, 281, 180, 262, 171, 230, 121, 197, 200, 172, 296, 157, 213, 137, 177, 201, 222, 155, 182, 172, 204,
         241, 198, 195]



y = []
x = []
i = 0

for n in lista:
    x.append(i)
    y.append(n)
    i += 1

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
plt.legend()


# Construtor do Gráfico
plt.show()