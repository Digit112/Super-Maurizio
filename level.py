import pygame as pg


from sprite import Sprite

ground = Sprite("brick_ground")

class Level(pg.sprite.Sprite):

	def __init__(self):

		super().__init__()

		self.surf = pg.Surface((1920, 1080))


class Block(pg.sprite.Sprite):

	def __init__(self):

		super().__init__()

		pass


class Ground(pg.sprite.Sprite):


	def __init__(self):

		super().__init__()

		self.image = ground.sprite
		self.surf = pg.Surface((1920, 1080), pg.SRCALPHA, 32)
		self.mask = pg.mask.from_surface(self.surf)
		self.rect = self.image.get_rect(topleft=(0,900))
		
		self.dt = 0

		self.w, self.h = self.image.get_size()

		self.last_added_coord = [(self.w*i, 0) for i in range(5)]

		self.create_ground()

	def create_ground(self):
		
		for i in self.last_added_coord:

			self.surf.blit(self.image, i)

		self.rect = self.surf.get_rect(topleft=(0,900))

	def move(self, mv):

		if mv:
			
			self.rect.x -= 5 * self.dt * 100

	def draw(self, screen):

		screen.blit(self.surf, self.rect)
