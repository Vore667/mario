import pygame
from pygame.locals import *
pygame.init()

pygame.display.set_caption("mario bros", "mini mario.png")
fenetre = pygame.display.set_mode((1030, 514))

fond = pygame.image.load("fond1.png").convert()
fenetre.blit(fond, (0,0))

perso = pygame.image.load("mini mario.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)
position_perso = position_perso.move(25,397)

pygame.display.flip()
continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événements
		if event.type == pygame.QUIT:
			continuer = 0
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				#On gauche le perso
				position_perso = position_perso.move(-3,0)
				pygame.display.flip()
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				#On droite le perso
				position_perso = position_perso.move(3,0)
		

	fenetre.blit(fond, (0,0))	
	fenetre.blit(perso, position_perso)
	pygame.display.flip()
