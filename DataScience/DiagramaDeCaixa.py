# boxplot - diagrama de caixas

from random import randint as r

import matplotlib.pyplot as plt

vetor = []

for i in range(0,100,4):
    n = r(0,50)
    vetor.append(n)

plt.bar(vetor,5)
plt.show()




