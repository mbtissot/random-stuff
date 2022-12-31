import numpy
from PIL import Image
import random

HEIGHT, WIDTH = 1024, 1024 # Defining width and height for the 'random' case.
# Defining some basic colors to use as constants, instead of typing their RGB code everytime
RED =      '255\t0\t0'
GREEN =    '0\t255\t0'
BLUE =     '0\t0\t255'
YELLOW =   '255\t255\t0'
WHITE =    '255\t255\t255'
BLACK =    '0\t0\t0'


def distance(x1, x2, y1, y2, norm): # This calculates the distance, according to some n-norm.
	# If you want to use Manhattan distance, you can call this function using norm=1.]
	# If you want the 'standard' 2D-distance, call distance with norm=2
	return ((abs(x1-x2))**norm + (abs(y1-y2))**norm)**(1/norm)

def fillseeds(seeds, grid):
	# This functions puts the seeds on the image as black
	print("Neighbours just called fillSeeds")
	for i in range(len(seeds)):
		grid[seeds[i][0]][seeds[i][1]] = BLACK
	return renderCircleSeed(seeds, grid, 7)

def renderCircleSeed(seeds, grid, radius):
	# This function renders a circle of radius='radius' on the image (because its hard to see individual pixels)
	print("fillSeeds just called renderCircleSeed")
	for seed in seeds:
		for i in range(seed[0]-radius, seed[0]+radius):
			for j in range(seed[1]-radius, seed[1]+radius):
				if (seed[0]-radius<0 or seed[0]+radius>HEIGHT or seed[1]-radius<0 or seed[1]+radius>WIDTH):
					continue # this is a check for boundary cases. If your seed is at the border of the
					# image, this for-loops would return something out of bounds. So this check is necessary
				#dist = (i-seed[0])**2 + (j-seed[1])**2
				dist = distance(i, seed[0], j, seed[1], 1.8) # Using norm=1.8 is the ideal way to print a circle
				# on the image. Otherwise, it'll be a 'squary-circle'
				if dist<=radius:
					grid[i][j] = BLACK
	return writeToPPM(grid)

def defineNeighbours(seeds, grid, colors):
	# This function defines the color of each pixel, based on their closest seed.
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
	# This function generates a random color to be the color of one 'neighbourhood'
	cor = str(random.randint(0, 255))+'\t'+str(random.randint(0, 255))+'\t'+str(random.randint(0, 255))
	return cor

def writeToPPM(grid):
	# THis functions just writes everything to the .ppm file
	print("Started writing to file")
	with open('output.ppm', 'w') as f:
		# Beggining of header
		f.write("P3\n") # Defining the type of PPM.
		f.write(str(WIDTH) + ' ' + str(HEIGHT) + "\n")
		f.write('255\n') # max value
		# End of header
		k=0
		# This section actually 'paints' the image.
		for i in range(HEIGHT):
			for j in range(WIDTH):
				f.write(str(grid[i][j]))
				f.write('\n')
	print("Done")



def config(configuration: str, configtype=None, SEED_NUM=0):
	# This function is the one who chooses which config you want ('random' or 'wigner-seitz')
	if configuration=="random":
		# If you want random: generates grid, colors and seeds. Then calls the other functions
		grid = [[0 for j in range(WIDTH)] for i in range(HEIGHT)]
		colors = [randomColor() for i in range(SEED_NUM)]
		seeds = [(random.randint(0, HEIGHT-1), random.randint(0, WIDTH-1)) for i in range(SEED_NUM)]
		defineNeighbours(seeds, grid, colors)
	elif configuration=="wigner-seitz":
		# If you want Wigner-Seitz, you have to choose the lattice layout.
		# At the moment, only 'square' lattices are available.
		if configtype=="square":
			seeds = [(i, j) for i in range(0, 1025, 256) for j in range(0, 1025, 256)]
			colors = ['255\t255\t255' for i in range(len(seeds))] # every color is white
			colors[12] = '105\t105\t105' # except one neighbourhood, which is grey.
			SEED_NUM = len(seeds)
			grid = [[0 for j in range(1025)] for i in range(1025)]
			defineNeighbours(seeds, grid, colors)
		elif configtype=="hexagonal":
			print('cai aqui')
			#to be done
			return

# If you want to create an image of a random Voronoi diagram:
config("random", SEED_NUM=16)

# If you want to create an image of a Wigner-Seitz cell inside a square lattice:
#config("wigner-seitz", "square")

