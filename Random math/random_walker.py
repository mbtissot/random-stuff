'''Roda com ~$ python nome_do_arquivo.py (se teu 'python' for direto p 3.x.x+)
ou com ~$ python3 nome_do_arquivo.py
'''


import time
import random

passos = 20
tamanho = 25
character = '■'
meio = (tamanho-1)/2
camin = [' ' for i in range(tamanho)]
camin2 = camin.copy()
camin[int(meio)]  = character
camin2[int(meio)] = '0'
print('[' + ''.join(camin2) + ']')


for i in range(passos+1):
    print('['+''.join(camin)+']' + '\r', end='')
    k = random.choice([-1, 1])
    pos = camin.index(character)
    if k == 1:
        camin[pos+1] = character
        camin[pos] = ' '
    elif k==-1:
        camin[pos-1] = character
        camin[pos] = ' '
    time.sleep(0.1)
print('')
print('Posição final: ', camin.index(character)-int(meio)-1)
