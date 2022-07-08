import time
import random
 
passos = 20
tamanho = 25
character = '■'
 
camin = [' ' for i in range(tamanho)]
camin[int((tamanho-1)/2)] = character
#print(camin)
'''print('[' + ''.join(camin) + ']')'''
 
for i in range(passos):
    k = random.choice([-1, 1])
    pos = camin.index(character)
    if k == 1:
        camin[pos+1] = character
        camin[pos] = ' '
    elif k==-1:
        camin[pos-1] = character
        camin[pos] = ' '
    print('['+''.join(camin)+']' + '\r', end='')
    time.sleep(0.2)