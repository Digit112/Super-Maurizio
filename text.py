import pygame as pg


class Text:

	def __init__(self):


		self.image = pg.Surface((356,128), pg.SRCALPHA, 32)
		self.rect = self.image.get_rect()

		self.font = pg.font.Font("assets/font/PressStart2P-vaV7.ttf", 10)

		self.speech_bubble = pg.draw.rect(self.image, (0,0,0), (0,0,128,64))

		self.text = None
		self.text_render = None
		self.text_counter = 1
		self.text_timer = 0

	def render_text(self, text):

		self.text = text
		self.text_render = self.font.render(text[0:self.text_counter], True, (255,255,255))
		
		if self.text_timer <= 30:
			self.text_timer += 1
		else:
			self.text_counter += 1
			self.text_timer = 0

		text_rect = self.text_render.get_rect(center=self.speech_bubble.center)

		self.speech_bubble = pg.draw.rect(self.image, (0,0,0), (0,0,len(text)+168,len(text)+64))
		self.image.blit(self.text_render, (self.speech_bubble.center[0]-len(text[0:self.text_counter]*5),self.speech_bubble.center[1]-10))

	def draw(self, screen, ch_pos, text):

		self.image.fill(0)

		self.render_text(text)
		screen.blit(self.image, (ch_pos[0], ch_pos[1]-90))



