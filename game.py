import pygame
from player import Player
from champi import Champi

class Game:
    def __init__(self):
        self.all_players =pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_champis = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_champi()

    def check_collision(self, sprite, group):
    	return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_champi(self):
    	champi = Champi(self)
    	self.all_champis.add(champi)