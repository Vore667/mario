import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health=1
        self.max_health=3
        self.velocity=2
        self.attack=3
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('mini mario.png')
        self.rect = self.image.get_rect()
        self.rect.x=25
        self.rect.y=397

    def lunch_projectile(self):
    	self.all_projectiles.add(Projectile(self))


    def move_right(self):
    	if not self.game.check_collision(self, self.game.all_champis):
    		self.rect.x += self.velocity

    def move_left(self):
    	self.rect.x -= self.velocity