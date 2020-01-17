# boxplot - diagrama de caixas

import matplotlib.pyplot as plt
from random import randint as r

vetor = []

for i in range(0,100,4):
    n = r(0,50)
    vetor.append(n)

plt.bar(vetor)
plt.show()




