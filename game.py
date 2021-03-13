import pygame, sys, math, random, os

pygame.init()
FPS = 60
clock = pygame.time.Clock()
WIN_SIZE = WIN_WIDTH, WIN_HEIGHT = 800, 600
screen = pygame.display.set_mode((WIN_SIZE), pygame.RESIZABLE)
font = pygame.font.Font("freesansbold.ttf",13)
#	IMAGES

#	COLORS
BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
GREEN = 0,128,0
BLUE = 0,255,255

covid_img = pygame.image.load(os.path.abspath('C:/Users/Admin/Documents/OperationsGoGoGO/images/covid.png'))

def rotate(mx,my):
	pass

class people:
	RADIUS = 15
	def __init__(self):
		self.x = 0
		self.y = 0
		self.movingRight = False
		self.movingLeft = False
		self.movingDown = False
		self.movingUp = False
		self.spawn_quadrant = {'right-top': False,'right-bottom':False,'left-top':False,'left-bottom':False,'bottom-right':False,'bottom-left':False,'top-right':False,'top-left':False}

	def where_spawn(self):
		spawn_coordinates = []
		sides = random.randint(1,4)

		if sides == 1:			# 	UP
			self.x = random.randint(0,WIN_WIDTH)
			self.y = WIN_HEIGHT - WIN_HEIGHT
			if self.x <= WIN_WIDTH//2:
				self.spawn_quadrant['top-left'] = True
			else:
				self.spawn_quadrant['top-right'] = True
		if sides == 2:			#	RIGHT
			self.x = WIN_WIDTH
			self.y = random.randint(0,WIN_HEIGHT)

			if self.y <= WIN_HEIGHT//2:
				self.spawn_quadrant['right-top'] = True
			else:
				self.spawn_quadrant['right-bottom'] = True
		if sides == 3:			#	BOTTOM
			self.x = random.randint(0,WIN_WIDTH)
			self.y = WIN_HEIGHT

			if self.x <= WIN_WIDTH//2:
				self.spawn_quadrant['bottom-left'] = True
			else:
				self.spawn_quadrant['bottom-right'] = True
		if sides == 4:			#	LEFT
			self.x = 0
			self.y = random.randint(0,WIN_HEIGHT)

			if self.y <= WIN_HEIGHT//2:
				self.spawn_quadrant['left-top'] = True
			else:
				self.spawn_quadrant['left-bottom'] = True


	def delete(self):
		delete = False
		if self.x < 0 or self.x > WIN_WIDTH or self.y > WIN_HEIGHT or self.y < 0:
			delete = True
		return delete

	def directions(self):
		fiftyfiftyX = random.randint(1,3)			# 	1 = RIGHT 2 = LEFT
		fiftyfiftyY = random.randint(1,3)			#	1 = UP 2 = DOWN 3 = NOTHING

		if self.spawn_quadrant['left-top'] == True:		
			if fiftyfiftyX == 1 and fiftyfiftyY == 3:	# STRAIGHT RIGHT
				self.movingRight = True
			if fiftyfiftyX == 1 and fiftyfiftyY == 2:	# RIGHT DOWN
				self.movingRight = True
				self.movingDown = True

		if self.spawn_quadrant['left-bottom'] == True:
			if fiftyfiftyX == 1 and fiftyfiftyY == 3:	# STRAIGHT RIGHT
				self.movingRight = True
			if fiftyfiftyX == 2 and fiftyfiftyY == 1:	#	LEFT UP
				self.movingLeft = True
				self.movingUp = True

		if self.spawn_quadrant['bottom-left'] == True:
			if fiftyfiftyX == 1 and fiftyfiftyY == 1:	# RIGHT UP
				self.movingRight = True
				self.movingUp = True
			if fiftyfiftyX == 1 and fiftyfiftyY == 3:	# STRAIGHT RIGHT
				self.movingRight = True

		if self.spawn_quadrant['bottom-right'] == True:
			if fiftyfiftyX == 1 and fiftyfiftyY == 1:	# RIGHT UP
				self.movingRight = True
				self.movingUp = True
			if fiftyfiftyX == 2 and fiftyfiftyY == 1:	#	LEFT UP
				self.movingLeft = True
				self.movingUp = True

		if self.spawn_quadrant['right-bottom'] == True:
			if fiftyfiftyX == 2 and fiftyfiftyY == 3:	# LEFT
				self.movingLeft = True
			if fiftyfiftyX == 2 and fiftyfiftyY == 1:	#	LEFT UP
				self.movingLeft = True
				self.movingUp = True

		if self.spawn_quadrant['right-top'] == True:
			if fiftyfiftyX == 2 and fiftyfiftyY == 3:	# LEFT
				self.movingLeft = True
			if fiftyfiftyX == 2 and fiftyfiftyY == 2:	# DOWN LEFT
				self.movingLeft = True
				self.movingDown = True
		if self.spawn_quadrant['top-right'] == True:
			if fiftyfiftyX == 3 and fiftyfiftyY == 2:	# DOWN
				self.movingDown = True
			if fiftyfiftyX == 1 and fiftyfiftyY == 2:	# RIGHT DOWN
				self.movingRight = True
				self.movingDown = True
		if self.spawn_quadrant['top-left'] == True:
			if fiftyfiftyX == 3 and fiftyfiftyY == 2:	# DOWN
				self.movingDown = True
			if fiftyfiftyX == 2 and fiftyfiftyY == 2:	# DOWN LEFT
				self.movingLeft = True
				self.movingDown = True
		print(self.spawn_quadrant)

	def draw(self):
		if self.delete() == False:
			self.player = pygame.draw.circle(screen, BLACK, (self.x,self.y), self.RADIUS)
	
	def move(self):
		horizontalSpeed = 1
		verticalSpeed = 1
		
		player_movement = [0,0]
		if self.movingRight == True:
			player_movement[0] += horizontalSpeed
		if self.movingLeft == True:
			player_movement[0] -= horizontalSpeed
		if self.movingDown == True:
			player_movement[1] += verticalSpeed
		if self.movingUp == True:
			player_movement[1] -= verticalSpeed
		self.x += player_movement[0]
		self.y += player_movement[1]

class Virus:
 	"""docstring for Virus"""
 	def __init__(self):
 		pass
 	def sneeze(self):
 		pass	

def spawn(amount):
	spawn.players = [people() for i in range(amount)]

	for player in spawn.players:
		if player.delete() == True:
			pass
		player.where_spawn()
		player.directions()

def main():
	running = True
	spawn(50)
	while running:							# game loop
		screen.fill(WHITE)					# BACKGROUND COLOR
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
				break
		
		for player in spawn.players:
			player.move()
			player.draw()

		clock.tick(FPS)
		pygame.display.update()
main()




