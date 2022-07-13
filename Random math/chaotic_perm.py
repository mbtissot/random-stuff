import numpy as np
from random import *

n = 10000
count = 0
for j in range(n+1):
    lista1 = [i for i in range(100)]
    for i in range(len(lista1)):
        k = choice(lista1)
        if i == k:
            count = count+1
            break        

print(1/(1-(count/(n+1))))
print(np.exp(1))
print(f"Erro = {np.abs(((1 - count/n)-np.exp(-1))/np.exp(-1))}%")


