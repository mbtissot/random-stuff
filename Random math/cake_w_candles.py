import random as rand

n = 1000000
success = 0
for i in range(n):
	c1 = rand.random()
	c2 = rand.random()
	k = rand.random()
	if ((c1<k) and (k<c2)) or ((c2<k) and (k<c1)):
		success = success+1

print(success/n)