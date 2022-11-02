import pygame as pg
import sys

class SpriteSheet:

	def __init__(self, filename):

		self.sheet = pg.image.load(filename).convert_alpha()

	def image_at(self, rectangle):

		rect = pg.Rect(rectangle)
		image = pg.Surface(rect.size, pg.SRCALPHA).convert_alpha()

		image.blit(self.sheet, (0,0), rect)

		return image.convert_alpha()

	def scale_image(self,image,scale,up=False,down=False):
		scale_by = (1,1)
		if up:
			scale_by = (image.get_width() * scale, image.get_height() * scale)
		if down:
			scale_by = (image.get_width() // scale, image.get_height() // scale)

		if up and down:
			return image.convert_alpha()

		return pg.transform.scale(image, scale_by).convert_alpha()


