import pygame as pg
import sys
from spritesheet import SpriteSheet
pg.init()
screen = pg.display.set_mode((1280,720))


ss = SpriteSheet("spritesheetghost.png")

sprite_loc = {

	"bg": (640,16,50,50),
	"wall": (510,80,50,47),
	"ch_right":(210,220,110,190),
	"ch_left":(10,220,110,190),
	"ch_down":(16,80,31,55),
	"ch_up":(64,80,31,55),
	"ch_arm":(112,16,4,22),
	"ch_light":(130,16,32,85),
	"ch_aura":(16,144,183,94)
	}



while 1:

	for e in pg.event.get():

		if e.type == pg.QUIT:
			pg.quit()
			sys.exit()

	screen.fill((1,100,1))
	screen.blit(ss.scale_image(ss.image_at(sprite_loc["ch_right"]), 2, up=True).convert_alpha(), (200,200))
	
	pg.display.flip()

