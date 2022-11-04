import pygame as pg
import random

from sprite import Sprite

ground = Sprite("brick_ground")

cloud = pg.image.load("assets/img/mauriziocloudlarge.png").convert_alpha()
cloud_size = cl_w, cl_h = cloud.get_size()
cloud_sizes = [pg.transform.scale(cloud, (cl_w//3,cl_h//3)), pg.transform.scale(cloud, (cl_w//2,cl_h//2)), pg.transform.scale(cloud, (cl_w//4,cl_h//4))]

ground_map = [0,0,0,0,0,0,0,0,0,0]

question_blocks = Sprite("question_block")
ground_block = Sprite("brick_block")

block_shapes = [0,0,1,1,1,0,0]


class Level(pg.sprite.Sprite):

	def __init__(self):

		super().__init__()

		self.surf = pg.Surface((1920, 1080))


class Block(pg.sprite.Sprite):

	def __init__(self):

		super().__init__()

		pass

class Cloud(pg.sprite.Sprite):

	def __init__(self):

		super().__init__()

		self.image = random.choice(cloud_sizes)

		self.rect = self.image.get_rect(center=(random.randint(2000,2100), random.randint(100,450)))

		self.size = self.width, self.height = self.image.get_size()

		if self.size == (120,80):
			self._layer = 1
			self.rect.y = random.randint(300,350)
		elif self.size == (160,106):
			self._layer = 2
			self.rect.y = random.randint(200,250)
		else:
			self._layer = 3

		self.speed = random.uniform(0.4, 1)
		self.dt = 0

	def draw(self,screen):

		screen.blit(self.image,self.rect)

class Cloud_handler(pg.sprite.Sprite):

	def __init__(self):

		self.clouds = pg.sprite.LayeredUpdates()
		self.dt = 0
		self.cloud_count = 0
		#for c in self.clouds:

	def move(self,speed, mv):

		if self.cloud_count == 100 and len(self.clouds) <= 10:
			self.clouds.add(Cloud())
			self.cloud_count = 0
		else:
			self.cloud_count += 1

		for i in self.clouds:
			i.dt = self.dt 
			i.rect.x -= i.speed 
			if i.rect.x < 0 - i.width:
				i.kill()
				self.clouds.add(Cloud())

class Tile(pg.sprite.Sprite):

	def __init__(self, img, tile_group):

		super().__init__(tile_group)

		self.image = img
		self.rect = self.image.get_rect()
		self.width, self.height = self.image.get_size()

class Blocks(pg.sprite.Sprite):

	def __init__(self):

		self.blocks = pg.sprite.Group()
		self.dt = 0
		self.block_count = 0
		self.speed = 6

		self.create_blocks()

	def create_blocks(self):

		if not len(self.blocks):


			for i in block_shapes:

				if i == 1:
					Tile(question_blocks.sprite, self.blocks)
				if i == 0:
					Tile(ground_block.sprite, self.blocks)

		x = 600

		for block in self.blocks:

			block.rect.topleft = (x,400)
			x += block.width

	def move(self, speed, mv):

		if mv:
			for b in self.blocks:

				b.rect.x -= self.speed * self.dt * 100



class Ground(pg.sprite.Sprite):


	def __init__(self):

		super().__init__()

		self.image = ground.sprite
		self.surf = pg.Surface((1920, 1080), pg.SRCALPHA, 32)
		self.mask = pg.mask.from_surface(self.surf)
		self.rect = self.image.get_rect(topleft=(0,900))
		
		self.dt = 0

		self.w, self.h = self.image.get_size()

		self.tiles = pg.sprite.Group()
		self.speed = 6

		self.create_ground()



	def create_ground(self):
		
		if not len(self.tiles):
			for i in ground_map:
				Tile(self.image, self.tiles)


		x = 0
		for i in self.tiles:
			i.rect = i.image.get_rect(topleft=(x, 900))
			x += i.width
		#self.rect = self.surf.get_rect(topleft=(0,900))

	def move(self, mv):

		if mv:
			for i in self.tiles:

				i.rect.x -= self.speed * self.dt * 100
	# def draw(self, screen):

	# 	if self.rect.x :
	# 		self.create_ground()


	# 	screen.blit(self.surf, self.rect)
