import pygame as pg
import random
import math
import os, sys


from constants import *


pg.init()
screen = pg.display.set_mode((size))
clock = pg.time.Clock()


from level import *
from character import Character
from text import Text

bg = pg.image.load("assets/img/bg.png").convert()

ground = Ground()
chara = Character()
blocks = Blocks()

cl_handler = Cloud_handler()
txt = Text()

groups = [
	
	ground.tiles,
	cl_handler.clouds,
	blocks.blocks


]
class Game:


	def __init__(self):

		self.screen = screen
		self.dt = 0

	def run(self):

		while 1:

			for e in pg.event.get():

				if e.type == pg.QUIT:

					pg.quit()
					sys.exit()


			screen.fill((99,155,255))

			k = pg.key.get_pressed()

			self.set_delta()
			self.event_move(k)
			self.event_collision()
			#screen.blit(bg, (0,0))
			self.draw_sprites()
			#txt.draw(screen, ch.rect, "asasdgasdgasdgajksdbkjasbdgkasdbgkjdasd")

			pg.display.flip()

			self.dt = clock.tick(FPS) / 1000

	def draw_sprites(self):

			chara.draw(screen)
			[gr.draw(screen) for gr in groups]
			# g.tiles.draw(screen)
			# cl_handler.clouds.draw(screen)

	def set_delta(self):

		chara.dt = self.dt
		ground.dt = self.dt
		cl_handler.dt = self.dt
		blocks.dt = self.dt

	def event_move(self, k):

		chara.move(k)
		ground.move(chara.is_moving)
		blocks.move(ground.speed, chara.is_moving)
		cl_handler.move(chara.is_moving, ground.speed)

	def event_collision(self):

		for b in blocks.blocks:

			if chara.rect.colliderect(b.rect):

				chara.collide_block(b.rect)





game = Game()

if __name__ == "__main__":

	game.run()
