import pygame, sys, math, random, os

pygame.init()
FPS = 60
clock = pygame.time.Clock()
WIN_SIZE = WIN_WIDTH, WIN_HEIGHT = 800, 600
screen = pygame.display.set_mode((WIN_SIZE), pygame.RESIZABLE)
font = pygame.font.Font("freesansbold.ttf",13)
#	COLORS
BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
GREEN = 0,128,0
BLUE = 0,255,255
#	IMAGES
covid_img = pygame.image.load(os.path.abspath('C:/Users/Admin/Documents/Operation-GoGoGO/images/covidv3.png'))
covid_img = pygame.transform.scale(covid_img,(50,29))
covid_img.convert_alpha()
covid_mask = pygame.mask.from_surface(covid_img)
covid_rect = covid_mask.get_rect()

vaccine_img = pygame.image.load(os.path.abspath('C:/Users/Admin/Documents/Operation-GoGoGO/images/vaccine.png'))
vaccine_img.convert_alpha()
vaccine_mask = pygame.mask.from_surface(vaccine_img)
vaccine_rect = vaccine_mask.get_rect()

class Virus:
 	"""docstring for Virus"""
 	def __init__(self):
 		self.x = 0
 		self.y = 0
 		self.angle = 0
 		self.power = 0
 		self.mouse_hold = False
 		self.mouse_hold_time = 0

 	def mouse_hold_funct(self):
 		if self.mouse_hold == True:
 			self.mouse_hold_time += 1
 			self.power += 0.5
 			print(self.power)
 		else:
 			self.power = 0
 			self.mouse_hold = False
 			self.mouse_hold_time = 0

 	def mouse_img(self,mx,my):
 		screen.blit(vaccine_img , (mx - (vaccine_rect.width//2.5), my - (vaccine_rect.height) + 10))

 	def sneeze(self):
 		pass

 	def draw(self,mx,my):
 		self.mx = mx
 		self.my = my
 		self.angle = math.atan2(self.my - (covid_rect.width//2), self.mx - (covid_rect.height//2))
 		screen.blit(covid_img, (self.x,self.y))

 	def aim(self,mx,my):
 		laser = pygame.draw.line(screen,RED, (covid_rect.width//2,covid_rect.height//2),(mx,my))

class people:
	RADIUS = 15
	def __init__(self):
		self.x = 0
		self.y = 0
		self.movingRight = False
		self.movingLeft = False
		self.movingDown = False
		self.movingUp = False
		self.infected = False
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

	
		if fiftyfiftyX == 1 and fiftyfiftyY == 3:	# 	STRAIGHT RIGHT
			self.movingRight = True
		if fiftyfiftyX == 1 and fiftyfiftyY == 2:	# 	RIGHT DOWN
			self.movingRight = True
			self.movingDown = True

		if fiftyfiftyX == 2 and fiftyfiftyY == 1:	#	LEFT UP
			self.movingLeft = True
			self.movingUp = True

		if fiftyfiftyX == 1 and fiftyfiftyY == 1:	# 	RIGHT UP
			self.movingRight = True
			self.movingUp = True

		if fiftyfiftyX == 2 and fiftyfiftyY == 3:	# 	LEFT
			self.movingLeft = True

		if fiftyfiftyX == 2 and fiftyfiftyY == 2:	# 	DOWN LEFT
			self.movingLeft = True
			self.movingDown = True
		
		if fiftyfiftyX == 3 and fiftyfiftyY == 2:	# 	DOWN
			self.movingDown = True
		
		if fiftyfiftyX == 3 and fiftyfiftyY == 1:	#	UP
			self.movingUp = True
		if fiftyfiftyX == 3 and fiftyfiftyY == 3:
			halfx = random.randint(1,2)
			halfy = random.randint(1,2)
			if halfx == 1:
				self.movingRight = True
			else:
				self.movingLeft = True
			if halfy == 1:
				self.movingDown = True
			else:
				self.movingUp = True

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
	virus1= Virus()
	LEFTCLICK = 1
	while running:							# game loop
		screen.fill(WHITE)					# BACKGROUND COLOR
		mx,my = pygame.mouse.get_pos()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
				break
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == LEFTCLICK:
					virus1.mouse_hold = True
			if event.type == pygame.MOUSEBUTTONUP:
				if event.button == LEFTCLICK:
					virus1.mouse_hold = False

		
		for player in spawn.players:
			player.move()
			player.draw()

		virus1.draw(mx,my)
		virus1.mouse_hold_funct()
		virus1.aim(mx,my)
		virus1.mouse_img(mx,my)

		clock.tick(FPS)
		pygame.display.update()
main()




