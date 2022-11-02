import pygame as pg
import sys
from spritesheet import SpriteSheet


ss = SpriteSheet("supermauriziospritesheetterrain01large.png")

class Sprite(pg.sprite.Sprite):

	def __init__(self, sprite_name, size=1, up=False, down=False):

		super().__init__()

		self.sprite_loc =  {

			"brick_ground": (0,0,479,479)
		}

		self.type = sprite_name
		self.sprite = ss.image_at(self.sprite_loc[sprite_name])
		
		if up or down:
			self.sprite = self.sprite_scaled(size,up,down)

		self.image = self.sprite
		self.rect = self.sprite.get_rect(center=(0,0))
		self.mask = pg.mask.from_surface(self.image, 0)
		self.w = self.sprite.get_width()
		self.h = self.sprite.get_height()

	def sprite_scaled(self, scale, up, down):

		return ss.scale_image(self.sprite, 2, up, down)

