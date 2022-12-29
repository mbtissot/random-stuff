import numpy
from PIL import Image
import random

HEIGHT, WIDTH = 1025, 1025
WHITE = [255, 255, 255]
BLACK = [0,     0,   0]

SEED_NUM = 16

#colors = [[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)] for i in range(SEED_NUM)]

global grid
grid = numpy.zeros((HEIGHT, WIDTH, 3), dtype=numpy.uint8)

#for i in range(SEED_NUM):
#	seeds.append((random.randint(0, HEIGHT-1), random.randint(0, WIDTH-1)))

def fillseeds(seeds, grid):
	for i in range(SEED_NUM):
		grid[seeds[i][0], seeds[i][1]] = [255, 255, 255]
	return renderCircleSeed(seeds, grid, 10)

def renderCircleSeed(seeds, grid, radius):
	for seed in seeds:
		for i in range(seed[0]-radius, seed[0]+radius):
			for j in range(seed[1]-radius, seed[1]+radius):
				distSquare = (i-seed[0])**2 + (j-seed[1])**2
				if distSquare<=radius*radius:
					grid[i, j] = WHITE
	return grid

def defineNeighbours(seeds, grid, colors):
	for i in range(WIDTH):
		for j in range(HEIGHT):
			listDistances = []
			for seed in range(len(seeds)):
				listDistances.append((i-seeds[seed][0])**2 + (j-seeds[seed][1])**2)
				index = listDistances.index(min(listDistances))
				grid[i, j] = colors[index]
	return fillseeds(seeds, grid)

#colors = []

#for i in range(0, 1025, 256):
#	for j in range(0, 1025, 256):
#		seeds.append((i, j))
#		colors.append([255, 255, 255])

#print(len(seeds))

#colors[12] = [105, 105, 105]

def config(configuration: str, configtype=None):
	if configuration=="random":
		colors = [[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)] for i in range(SEED_NUM)]
		seeds = [(random.randint(0, HEIGHT-1), random.randint(0, WIDTH-1)) for i in range(SEED_NUM)]
		print('vim aqui')
		Image.fromarray(defineNeighbours(seeds, grid, colors)).show()
	elif configuration=="wigner-seitz":
		if configtype=="square":
			seeds = [(i, j) for i in range(0, 1025, 256) for j in range(0, 1025, 256)]
			colors = [[255, 255, 255] for i in range(len(seeds))]
			colors[12] = [105, 105, 105]
		elif configtype=="hexagonal":
			print('cai aqui')
			#to be done
			return

config("random")