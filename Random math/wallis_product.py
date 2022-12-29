import numpy as np

wallis = 1
for i in range(2, 10000, 2):
	wallis = wallis * (i/(i-1)) * (i/(i+1)) 

print('Wallis pi =', wallis)
print('Pi on 2 = ', np.pi/2)



