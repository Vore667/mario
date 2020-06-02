import pygame
from game import Game
pygame.init()



pygame.display.set_caption("mario bros", 'mini mario.png')
screen = pygame.display.set_mode((1030, 514))


background = pygame.image.load('fond1.png')

game = Game()


running = True
while running:

    screen.blit(background, (0,0))
    screen.blit(game.player.image, game.player.rect)


    for projectile in game.player.all_projectiles:
        projectile.move()

    for champi in game.all_champis:
        champi.forward()

    game.player.all_projectiles.draw(screen)

    game.all_champis.draw(screen)


 
    pygame.display.flip()

    if game.pressed.get(pygame.K_RIGHT)and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.lunch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
 
