import pygame, sys, math, random, os
pygame.init()
FPS=60
clock=pygame.time.Clock()
game_name=pygame.display.set_caption('C-19')
WIN_SIZE=WIN_WIDTH, WIN_HEIGHT = 800, 600
screen=pygame.display.set_mode((WIN_SIZE), pygame.RESIZABLE)
font=pygame.font.Font("freesansbold.ttf",13)
#	COLORS
BLACK=0,0,0
WHITE=255,255,255
RED=255,0,0
GREEN=0,128,0
BLUE=0,255,255
#	IMAGES
covid_img=pygame.image.load(os.path.abspath('C:/Users/Admin/Documents/Operation-GoGoGO/covid.jpg'))
covid_img=pygame.transform.scale(covid_img,(50,50))
covid_img.convert_alpha()
game_icon=pygame.display.set_icon(covid_img)
covid_mask=pygame.mask.from_surface(covid_img)
covid_rect=covid_mask.get_rect()
vaccine_img=pygame.image.load(os.path.abspath('C:/Users/Admin/Documents/Operation-GoGoGO/images/vaccine.png'))
vaccine_img.convert_alpha()
vaccine_mask=pygame.mask.from_surface(vaccine_img)
vaccine_rect=vaccine_mask.get_rect()
one_second=0
time=0
time_list0=[0,10*FPS,20*FPS]
time_list1=[5*FPS,15*FPS,25*FPS]
secure_random = random.SystemRandom()
def draw_text(text, font, color, surface,x,y):
	textobj = font.render(text, 1, color)
	textrect = textobj.get_rect()
	textrect.topleft = (x,y)
	surface.blit(textobj, textrect)
class Virus():
 	RADIUS=8
 	def __init__(self,patient_1):
 		self.x=0
 		self.y=0
 		self.speed=6.5
 		self.first_fire=False
 		self.bullets=[]
 		self.patient_1=patient_1
 		# A transparent surface with per-pixel alpha.
 		self.surface=pygame.Surface((self.RADIUS*2,self.RADIUS*2), pygame.SRCALPHA)
 		self.alive=True
 		self.hitbox=pygame.Rect(self.x,self.y,self.RADIUS*2,self.RADIUS*2)
 		self.draw_hitbox=0
 		self.color=RED
 		self.left_click=False
 		self.on_air=False
 	def spawn_location(self):
 		if self.first_fire==False:
 			self.x=self.patient_1.x-self.patient_1.RADIUS//2
 			self.y=self.patient_1.y-self.patient_1.RADIUS//2
 	def center(self):		#	Center of Virus
 		self.centerX=self.x+self.RADIUS
 		self.centerY=self.y+self.RADIUS
 	def mouse_img(self):
 		screen.blit(vaccine_img,(self.mx, self.my))
 	def fire_funct(self):	#	BLIT MOVING COVID
 		if self.alive:
 			for bullet in self.bullets:
 				bulletspeed=self.speed
 				index=0
 				velx=math.cos(bullet[0])*bulletspeed
 				vely=math.sin(bullet[0])*bulletspeed
 				bullet[1]+=velx
 				bullet[2]+=vely
 				if bullet[1]<-200 or bullet[1]>WIN_WIDTH+200 or bullet[2]<-200 or bullet[2]>WIN_HEIGHT+200:
 					self.bullets.pop(index)
 				index+= 1
 				for projectile in self.bullets:
 					bullets1=pygame.transform.rotate(self.surface, 360-projectile[0]*57.29)
 					self.x=projectile[1]
 					self.y=projectile[2]
 	def draw(self):
 		if self.alive:
 			self.virus=pygame.draw.circle(screen, BLUE, (self.x + self.RADIUS,self.y + self.RADIUS), self.RADIUS)
 			screen.blit(self.surface,(self.x,self.y))
 		if self.x >(WIN_WIDTH+40) or self.x < -40 or self.y <-40 or self.y >640:
 			self.alive = False
 	def hitbox_funct(self):
 		self.hitbox=pygame.Rect(self.x,self.y,self.RADIUS*2,self.RADIUS*2)
 		#self.draw_hitbox=pygame.draw.rect(screen, self.color, self.hitbox,2)
 		#self.color=RED
 	def aim(self,mx,my):
 		self.mx = mx
 		self.my = my
 			#laser = pygame.draw.line(screen,GREEN, (self.centerX,self.centerY),(self.mx,self.my))
 	def calculations(self):
 		pass
 	def gameover(self):
 		if self.alive==False:
 			gameover_text=draw_text("Game over", font, RED, screen,WIN_WIDTH/2,WIN_HEIGHT/2-200)
class patient1():
	RADIUS = 15
	def __init__(self):
		self.x = WIN_WIDTH//2
		self.y = WIN_HEIGHT//2
		self.speed = 2
		self.spawn_location = {"left": [0,WIN_HEIGHT//2],"top": [WIN_WIDTH//2,0],"right":[WIN_WIDTH,WIN_HEIGHT//2],"bottom": [WIN_WIDTH//2,WIN_HEIGHT]}
		self.STARTING_POS = random.randint(1,4)
		self.alive = True
	def draw(self):
		if self.x in range(0,WIN_WIDTH) or self.y in range(0,WIN_HEIGHT) and self.alive:
			patient1 = pygame.draw.circle(screen, RED, (self.x,self.y), self.RADIUS)
		else:
			self.x = -10
			self.y = -10
	def spawn_location_random_and_movement(self):
		#	Spawn Locations
		if self.STARTING_POS == 1:
			self.x, self.y = self.spawn_location["left"]
		elif self.STARTING_POS == 2:
			self.x, self.y = self.spawn_location["top"]
		elif self.STARTING_POS == 3:
			self.x, self.y = self.spawn_location["right"]
		else:
			self.x,self.y = self.spawn_location["bottom"]
	def move(self):
		if self.STARTING_POS == 1:
			self.x += self.speed
		elif self.STARTING_POS == 2:
			self.y += self.speed
		elif self.STARTING_POS == 3:
			self.x -= self.speed
		else:
			self.y -= self.speed
class people:
	RADIUS = 15
	color=BLACK
	horizontalSpeed = secure_random.uniform(1,2)
	verticalSpeed = secure_random.uniform(1,2)
	def __init__(self):
		self.x = 0
		self.y = 0
		self.movingRight = False
		self.movingLeft = False
		self.movingDown = False
		self.movingUp = False
		self.infected = False
		self.spawn_quadrant = {"top":False,"bottom":False,"left":False,"right":False,}
		self.surface = pygame.Surface((self.RADIUS*2,self.RADIUS*2),pygame.SRCALPHA)
		self.hitbox = pygame.Rect(self.x,self.y,self.RADIUS*2,self.RADIUS*2)
		self.draw_hitbox=0
		self.alive=True
		self.has_been_counted=False
	def where_spawn(self):
		spawn_coordinates = []
		sides = random.randint(1,4)
		GAP_WIDTH=200
		GAP_HEIGHT=150
		if sides == 1:							#UP
			self.x = random.randint(GAP_WIDTH, GAP_WIDTH*2)
			self.y = WIN_HEIGHT - WIN_HEIGHT
			self.spawn_quadrant['top'] = True
		if sides == 2:			#	RIGHT
			self.x = WIN_WIDTH
			self.y = random.randint(GAP_HEIGHT, GAP_HEIGHT*2)
			self.spawn_quadrant['right'] = True
		if sides == 3:			#	BOTTOM
			self.x = random.randint(GAP_WIDTH, GAP_WIDTH*2)
			self.y = WIN_HEIGHT
			self.spawn_quadrant['bottom'] = True
		if sides == 4:			#	LEFT
			self.x = 0
			self.y = random.randint(GAP_HEIGHT, GAP_HEIGHT*2)
			self.spawn_quadrant['left'] = True
	def hitbox_funct(self):
 		self.hitbox = pygame.Rect(self.x,self.y,self.RADIUS*2,self.RADIUS*2)
 		#self.draw_hitbox = pygame.draw.rect(screen, RED, self.hitbox,2)
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
		if self.alive==True:
			self.player = pygame.draw.circle(screen, self.color, (self.x + self.RADIUS,self.y + self.RADIUS), self.RADIUS)
			screen.blit(self.surface,(self.x,self.y))
		if self.x >(WIN_WIDTH+40) or self.x < -40 or self.y <-40 or self.y >640:
			self.alive=False
		if self.infected==True:
			self.color=RED
	def move(self):
		player_movement = [0,0]
		if self.movingRight == True:
			player_movement[0] += self.horizontalSpeed
		if self.movingLeft == True:
			player_movement[0] -= self.horizontalSpeed
		if self.movingDown == True:
			player_movement[1] += self.verticalSpeed
		if self.movingUp == True:
			player_movement[1] -= self.verticalSpeed
		self.x += player_movement[0]
		self.y += player_movement[1]
def people_init(players):
	for player in players:#change player_list
		player.where_spawn()
		player.directions()
	return players # this function works
def is_collide(rect1,rect2):
	collide=rect1.colliderect(rect2)
	return collide
def main():
	global one_second, time, font
	players = [people() for i in range(30)]
	running=True
	people_infected=0
	time_score=0
	#	PATIENT 1 INIT
	patient_1=patient1()
	patient_1.spawn_location_random_and_movement()
	#	People_init
	people_1=people_init(players)
	#	VIRUS INIT
	virus1=Virus(patient_1)
	virus1.spawn_location()
	LEFTCLICK=1
	while running:	#	game loop
		screen.fill(WHITE)
		mx,my=pygame.mouse.get_pos()
		click=False
		playagain_rect = pygame.Rect(WIN_WIDTH/2,WIN_HEIGHT-400,100,50)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
				pygame.quit()
				sys.exit()
				break
			if event.type==pygame.MOUSEBUTTONUP:
				if event.button==LEFTCLICK:
					virus1.left_click=False
			if event.type==pygame.MOUSEBUTTONDOWN:
				if event.button==LEFTCLICK:#	POSITION OF VIRUS
					virus1.bullets.append([math.atan2((virus1.my)-(virus1.y),(virus1.mx)-(virus1.x)),(virus1.x),(virus1.y)])
					virus1.first_fire=True 	#fire = True
					virus1.left_click=True
					click = True
		if playagain_rect.collidepoint((mx, my)):
			if click and virus1.alive==False:
				virus1.x=WIN_WIDTH/2
				virus1.y=WIN_HEIGHT/2
				virus1.alive=True
		#	Patient loop
		patient_1.move()
		patient_1.draw()
		#	Virus Calculation
		virus1.center()
		#	VIRUS loop::starting move
		virus1.hitbox_funct()
		virus1.spawn_location()
		virus1.fire_funct()
		virus1.aim(mx,my)
		#virus1.mouse_img()
		'''	draw & move funct for each individual player'''
		for player in players:
			player.move()
			player.draw()
			player.hitbox_funct()
			collide=is_collide(virus1.hitbox, player.hitbox)
			if virus1.left_click==False:
				if collide==True and virus1.first_fire==1:
					virus1.color=GREEN
					virus1.x=player.x+(player.RADIUS//2)
					virus1.y=player.y+(player.RADIUS//2)
					player.infected=True
					# SCORE FUNCTION
					virus1.on_air=False
			else:
				collide=0
				virus1.on_air=True
			if player.infected==True and player.has_been_counted==False:
				time_score+=1
				if time_score==30:
					people_infected+=1
			if time_score>=32 and player.has_been_counted==False:
				time_score=0
				player.has_been_counted=True

		if virus1.alive==False:
			playagain_box  = pygame.draw.rect(screen, RED, playagain_rect,width=0,)
			playagain_button = draw_text('PLAY AGAIN', font, WHITE, screen, WIN_WIDTH/2, WIN_HEIGHT-400)
		virus1.draw()
		virus1.gameover()
		#	GAME UPDATES
		clock.tick(FPS)
		time+=1
		time_text=draw_text("Time: " + str(time), font, RED, screen, WIN_WIDTH/2,WIN_HEIGHT/2)
		score_text=draw_text("People infected: " + str(people_infected), font, RED, screen, WIN_WIDTH/2,WIN_HEIGHT/2 + 50)
		time_score_text=draw_text("time_Score: " + str(time_score), font, RED, screen, WIN_WIDTH/2,WIN_HEIGHT/2 + 100)
		#TEST STUFF
		pygame.display.update()
if __name__=='__main__':
	main()