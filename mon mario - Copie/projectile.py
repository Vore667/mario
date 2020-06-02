import pygame

class Projectile(pygame.sprite.Sprite):

	def __init__(self, player):
		super().__init__()
		self.velocity=5
		self.player=player
		self.image = pygame.image.load('bouldefeu.png')
		self.image = pygame.transform.scale(self.image, (15, 15))
		self.rect=self.image.get_rect()
		self.rect.x = player.rect.x + 10
		self.rect.y = player.rect.y + 10
		self.origin_image =self.image
		self.angle=0

	def remove(self):
		self.player.all_projectiles.remove(self)

	def rotate(self):
		self.angle += 12
		self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
		self.rect =self.image.get_rect(center=self.rect.center)

	def move(self):
		self.rect.x += self.velocity
		self.rotate()

		for champi in self.player.game.check_collision(self, self.player.game.all_champis):
			self.remove()

			champi.damage(self.player.attack)

		if self.rect.x > 1030:
			self.remove()
			print ("a")