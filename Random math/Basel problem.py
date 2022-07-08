import matplotlib.pyplot as plt
import numpy as np

qnts = 100

n = np.arange(1, qnts, 1)
valor_real = []
y = []
ysum = []

for i in n:
    valor_real.append((((np.pi)**2)/6))
    y.append(1/(i**2))
    
soma = 0    

for i in range(len(y)):
    soma = soma + y[i]
    ysum.append(soma)
    
plt.plot(n, valor_real, color='blue', label='pi²/6 ~ 1.64493407')
plt.plot(n, ysum, color='red', label='Sum of 1/n²')
plt.xticks(np.arange(0, 100, step=10))
plt.yticks(np.arange(1, 1.7, step=0.1))
plt.grid()
plt.legend()
plt.show()
    
    