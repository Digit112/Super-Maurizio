import pygame as pg
import os


nohat_dir = "assets/img/frames/maurizio_nohat/"
hat_dir = "assets/img/frames/maurizio_nohat/"

character_nohat = [pg.image.load(nohat_dir+i).convert_alpha() for i in os.listdir(nohat_dir)]
character_hat = [pg.image.load(hat_dir+i).convert_alpha() for i in os.listdir(hat_dir)]
character_nohat_reverse = [pg.transform.flip(i, True, False) for i in character_nohat]
character_hat_reverse = [pg.transform.flip(i, True, False) for i in character_hat]



class Character(pg.sprite.Sprite):

	def __init__(self):

		super().__init__()

		self.image = character_nohat[0]
		self.frames = character_nohat

		self.current_frame = 0
		self.frame_count = 0
		self.face = "r"

		self.scrolling = False

		self.mask = pg.mask.from_surface(self.image)
		self.rect = self.image.get_rect(midbottom=(10,900))

		self.dt = None
		self.speed = 5
		self.momentum = 0

		self.jumping = False
		self.jump_count = 15

		self.v = 10
		self.fall_momentum = 1
		self.jump_momentum = 3

		self.long_jump = False
		self.long_jump_counter = 0

		self.grounded = True

		self.walk_momentum = 0
		#self.mask_rect = pg.mask.from_surface(self.image)

	def update(self):
		pass

	def move(self, keys):

		up, left, right, space = keys[pg.K_UP] ,  keys[pg.K_LEFT] or keys[pg.K_a], keys[pg.K_RIGHT] or keys[pg.K_d], keys[pg.K_SPACE]

		if space and self.grounded and not self.jumping:

			self.grounded = False
			self.jumping = True
			

		if space and self.jumping:
			
			self.long_jump = True
			self.long_jump_counter += 5

		elif not space:

			self.long_jump_counter = 0
			self.long_jump = False


		if left and self.rect.x > 0:

			if self.face != "l":

				self.rect.x += self.walk_momentum
				self.face = "l"
				self.frames = character_nohat_reverse

			self.animate()

			self.rect.x -= self.walk_momentum + self.speed * self.dt * 60

			if self.walk_momentum < 10:

				self.walk_momentum += 0.4

		elif not left and not right and self.walk_momentum > 0 :

			self.walk_momentum -= 0.5

		if not left and not right:
			self.image = self.frames[0]

		if right:

			if self.face != "r":
				self.rect.x -= self.walk_momentum
				self.face = "r"
				self.frames = character_nohat

			self.animate()

			if self.rect.x < 500:
				self.rect.x += self.walk_momentum + self.speed * self.dt * 60
				self.is_moving = False

			self.scrolling = self.rect.x >= 500

			if self.walk_momentum < 10:

				self.walk_momentum += 0.4

		elif not left and not right and self.walk_momentum > 0:

			self.walk_momentum -= 0.5


		if self.jumping:

			self.jump()

		self.is_moving = right and self.scrolling


	def animate(self):

		if self.jumping:
			self.image = self.frames[1]
			return

		if self.frame_count == 10:

			self.current_frame = (self.current_frame + 1) % len(self.frames)
			self.image = self.frames[self.current_frame]
			self.frame_count = 0
		else:

			self.frame_count += 1

	def collide_block(self, hit):

		if self.rect.top <= hit.bottom:
			self.v -= 5
		if self.rect.left >= hit.right:
			self.x = hit.right
			return
			
	def jump(self):

		if self.jumping:

			if self.v > 0:
				f = (0.5 * self.jump_momentum * (self.v**2))

			else:
				f = -(0.5 * self.jump_momentum * (self.v**2))

			self.rect.y -= f / 3.2 * self.dt * 60 

			if self.long_jump:
				self.v -= 0.3
			else:
				self.v -= 0.6

			if self.rect.bottom > 900:

				self.rect.bottom = 900
				self.jumping = False
				self.grounded = True
				self.v = 10

			# if self.jump_count > 0:

			# 	self.rect.y -= (self.jump_count * abs(self.jump_count)) * self.jump_momentum * self.dt * 100

			# 	self.jump_count -= 1
			# 	self.fall_momentum += 0.1

			# 	if self.jump_momentum >= 0:

			# 		self.jump_momentum -= 0.0
			# else:

			# 	self.jumping = False
			# 	self.jump_count = 15
			# 	self.jump_momentum = 0.6




	def draw(self,screen):

		screen.blit(self.image, self.rect)

