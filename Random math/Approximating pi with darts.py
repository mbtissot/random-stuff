import matplotlib.pyplot as plt
import numpy as np
from numpy import random
l = 6.4
plt.matplotlib.rc('figure', figsize = (l,l*0.75)) # (width, height) in inches


N = 10000 # number of darts thrown

circlex = []
circley = []
squarex = []
squarey = []

r = 1

i = 1

while i <= N:
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    if (x**2 + y**2 <= r**2):
        circlex.append(x)
        circley.append(y)
    else:
        squarex.append(x)
        squarey.append(y)
    i += 1

pi = 4 * (len(circlex)) / float(N)

print('Pi is estimated to be =', pi)
print('Pi actually is =', np.pi)

plt.plot(circlex, circley, 'g.')
plt.plot(squarex, squarey, 'r.')
plt.grid()
plt.show()
