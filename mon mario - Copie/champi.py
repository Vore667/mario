import pygame


class Champi(pygame.sprite.Sprite):

	def __init__(self, game):
		super().__init__()
		self.game = game
		self.health = 1
		self.max_health =1
		self.attack = 5
		self.image = pygame.image.load("champi.png")
		self.rect = self.image.get_rect()
		self.rect.x = 1000
		self.rect.y = 400
		self.velocity = 1

	def damage(self, amount):

		self.health -= amount

		if self.health <= 0:
			self.rect.x += 50
			self.health = self.max_health


	def forward(self):
		if not self.game.check_collision(self, self.game.all_players):
			self.rect.x -= self.velocity