import numpy
from PIL import Image
import random

HEIGHT, WIDTH = 1024, 1024
RED =      '255\t0\t0'
GREEN =    '0\t255\t0'
BLUE =     '0\t0\t255'
YELLOW =   '255\t255\t0'
WHITE =    '255\t255\t255'
BLACK =    '0\t0\t0'


def distance(x1, x2, y1, y2, norm):
	return ((abs(x1-x2))**norm + (abs(y1-y2))**norm)**(1/norm)

def fillseeds(seeds, grid):
	print("Neighbours just called fillSeeds")
	for i in range(len(seeds)):
		grid[seeds[i][0]][seeds[i][1]] = BLACK
	return renderCircleSeed(seeds, grid, 7)

def renderCircleSeed(seeds, grid, radius):
	print("fillSeeds just called renderCircleSeed")
	for seed in seeds:
		for i in range(seed[0]-radius, seed[0]+radius):
			for j in range(seed[1]-radius, seed[1]+radius):
				if (seed[0]-radius<0 or seed[0]+radius>HEIGHT or seed[1]-radius<0 or seed[1]+radius>WIDTH):
					continue
				#dist = (i-seed[0])**2 + (j-seed[1])**2
				dist = distance(i, seed[0], j, seed[1], 1.8)
				if dist<=radius:
					grid[i][j] = BLACK
	return writeToPPM(grid)

def defineNeighbours(seeds, grid, colors):
	print("Define Neighbours")
	for i in range(HEIGHT):
		for j in range(WIDTH):
			listDistances = []
			for seed in range(len(seeds)):
				listDistances.append(distance(i, seeds[seed][0], j, seeds[seed][1], 2))
				index = listDistances.index(min(listDistances))
				grid[i][j] = colors[index]
	return fillseeds(seeds, grid)

def randomColor():
	cor = str(random.randint(0, 255))+'\t'+str(random.randint(0, 255))+'\t'+str(random.randint(0, 255))
	return cor

def writeToPPM(grid):
	print("Started writing to file")
	with open('output.ppm', 'w') as f:
		f.write("P3\n")
		f.write(str(WIDTH) + ' ' + str(HEIGHT) + "\n")
		f.write('255\n') # max value
		k=0
		for i in range(HEIGHT):
			for j in range(WIDTH):
				f.write(str(grid[i][j]))
				f.write('\n')
	print("Done")



def config(configuration: str, configtype=None, SEED_NUM=0):
	if configuration=="random":
		grid = [[0 for j in range(WIDTH)] for i in range(HEIGHT)]
		colors = [randomColor() for i in range(SEED_NUM)]
		seeds = [(random.randint(0, HEIGHT-1), random.randint(0, WIDTH-1)) for i in range(SEED_NUM)]
		defineNeighbours(seeds, grid, colors)
	elif configuration=="wigner-seitz":
		if configtype=="square":
			seeds = [(i, j) for i in range(0, 1025, 256) for j in range(0, 1025, 256)]
			colors = ['255\t255\t255' for i in range(len(seeds))]
			colors[12] = '105\t105\t105'
			SEED_NUM = 26
			grid = [[0 for j in range(1025)] for i in range(1025)]
			defineNeighbours(seeds, grid, colors)
		elif configtype=="hexagonal":
			print('cai aqui')
			#to be done
			return
#print(grid)
#config("wigner-seitz", "square")
config("random", SEED_NUM=16)



'''height = 10
width = 4
abc = [[0 for i in range(width)] for k in range(height)]
print(abc)

k=0
for i in range(height):
	for j in range(width):
		abc[i][j] = k
		k = k+1
print(abc)
'''