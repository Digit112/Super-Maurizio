import pygame as pg
import random
import math
import os, sys


from constants import *


pg.init()
screen = pg.display.set_mode((size))
clock = pg.time.Clock()


from level import Ground
from character import Character


bg = pg.image.load("assets/img/bg.png").convert()

g = Ground()
ch = Character()


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

			ch.dt = self.dt
			g.dt = self.dt

			k = pg.key.get_pressed()
			self.event_move(k)

			screen.blit(bg, (0,0))

			if not ch.jumping:
				ch.gravity(g.rect.colliderect(ch.rect))

			g.draw(screen)
			ch.draw(screen)

			pg.display.flip()
			self.dt = clock.tick(FPS) / 1000

	def event_move(self, k):

		ch.move(k)
		g.move(ch.is_moving)






game = Game()

if __name__ == "__main__":

	game.run()
